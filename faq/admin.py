from django.contrib import admin
from models import Question, Topic
from datetime import datetime


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'sort_order', )
    list_filter = ('language', )
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name', )}


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'language', 'topic', 'sort_order', 'created_by',
                    'created_on', 'updated_by', 'updated_on', 'status', )
    list_filter = ('language', 'status',)
    search_fields = ['question', 'answer']
    prepopulated_fields = {'slug': ('question', )}
    date_hierarchy = 'created_on'

    def save_model(self, request, obj, form, change):
        """ 
        Save the question's author.
        """
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

admin.site.register(Question, QuestionAdmin)
admin.site.register(Topic, TopicAdmin)
