from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Subquery
from django.shortcuts import render
from django.urls import path
from unfold.admin import ModelAdmin
from .models import AscensionRecord, FearScenario, UserDevice


@admin.register(AscensionRecord)
class AscensionRecordAdmin(ModelAdmin):
    list_display = ("user", "scenario", "target_level", "peak_hr", "timestamp")
    list_filter = ("target_level", "timestamp")
    search_fields = ("user__username", "scenario__name")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "orm-queries/",
                self.admin_site.admin_view(self.orm_queries_view),
                name="simulation_ascensionrecord_orm_queries",
            ),
        ]
        return custom_urls + urls

    def orm_queries_view(self, request):
        min_hr_raw = request.GET.get("min_hr", "").strip()

        join_queryset = (
            AscensionRecord.objects.select_related("user", "scenario")
            .values(
                "id",
                "user__username",
                "scenario__name",
                "target_level",
                "peak_hr",
                "end_hr",
                "timestamp",
            )
            .order_by("-timestamp")
        )
        join_sql = (
            "SELECT\n"
            "    ar.id,\n"
            "    u.username,\n"
            "    fs.name AS scenario,\n"
            "    ar.target_level,\n"
            "    ar.peak_hr,\n"
            "    ar.end_hr,\n"
            "    ar.timestamp\n"
            "FROM ascension_record ar\n"
            "LEFT OUTER JOIN auth_user u\n"
            "    ON (ar.user_id = u.id)\n"
            "LEFT OUTER JOIN fear_scenario fs\n"
            "    ON (ar.scenario_id = fs.id)\n"
            "ORDER BY ar.timestamp DESC"
        )

        inner_records = AscensionRecord.objects.exclude(user__isnull=True)
        where_clause = "WHERE ar.user_id IS NOT NULL"
        if min_hr_raw:
            try:
                min_hr = float(min_hr_raw)
                inner_records = inner_records.filter(peak_hr__gte=min_hr)
                where_clause = (
                    f"WHERE ar.user_id IS NOT NULL AND ar.peak_hr >= {min_hr}"
                )
            except ValueError:
                pass

        subquery_user_ids = inner_records.values("user_id").distinct()
        subquery_queryset = (
            User.objects.filter(id__in=Subquery(subquery_user_ids))
            .values("id", "username", "email", "is_staff")
            .order_by("username")
        )
        subquery_sql = (
            "SELECT\n"
            "    u.id,\n"
            "    u.username,\n"
            "    u.email,\n"
            "    u.is_staff\n"
            "FROM auth_user u\n"
            "WHERE u.id IN (\n"
            "    SELECT DISTINCT\n"
            "        ar.user_id\n"
            "    FROM ascension_record ar\n"
            f"    {where_clause}\n"
            ")\n"
            "ORDER BY u.username ASC"
        )

        context = {
            **self.admin_site.each_context(request),
            "title": "Django ORM JOIN & SUBQUERY Explorer",
            "join_records": join_queryset,
            "join_sql": join_sql,
            "subquery_users": subquery_queryset,
            "subquery_sql": subquery_sql,
            "min_hr": min_hr_raw,
            "scenario_count": FearScenario.objects.count(),
        }
        return render(request, "admin_orm_queries.html", context)

    @staticmethod
    def format_sql(raw_sql: str) -> str:
        formatted = raw_sql
        for kw in [
            " FROM ",
            " INNER JOIN ",
            " LEFT OUTER JOIN ",
            " WHERE ",
            " ORDER BY ",
        ]:
            formatted = formatted.replace(kw, f"\n{kw.strip()} ")
        formatted = formatted.replace("SELECT ", "SELECT\n    ")
        formatted = formatted.replace(", ", ",\n    ")
        formatted = formatted.replace(" ON (", "\n    ON (")
        formatted = formatted.replace(" IN (SELECT ", " IN (\n    SELECT\n        ")
        return formatted


@admin.register(FearScenario)
class FearScenarioAdmin(ModelAdmin):
    list_display = ("name", "category", "is_active", "created_by")
    list_filter = ("category", "is_active")
    search_fields = ("name", "category")


@admin.register(UserDevice)
class UserDeviceAdmin(ModelAdmin):
    list_display = ("device_name", "user", "mac_address", "is_active")
