from django.contrib import admin
from .models import Endpoint, MLAlgorithm, MLAlgorithmStatus, MLRequest, ABTest


@admin.register(Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'created_at']
    list_filter = ['owner', 'name']


@admin.register(MLAlgorithm)
class MLAlgorithmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent_endpoint', 'version', 'owner', 'created_at']
    list_filter = ['owner', 'parent_endpoint']


@admin.register(MLAlgorithmStatus)
class MLAlgorithmStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'active', 'parent_mlalgorithm', 'created_by', 'created_at']
    list_filter = ['created_by', 'status', 'parent_mlalgorithm']


@admin.register(MLRequest)
class MLRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent_mlalgorithm', 'created_at']
    list_filter = ['parent_mlalgorithm']


@admin.register(ABTest)
class ABTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_by', 'created_at', 'ended_at', 'summary', 'parent_mlalgorithm_1',
                    'parent_mlalgorithm_2']
    list_filter = ['parent_mlalgorithm_1', 'parent_mlalgorithm_2']
