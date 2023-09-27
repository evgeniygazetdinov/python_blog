from django.contrib import admin

# Register your models here.
from articles.models import Article, Author, Tag


@admin.register(Article)
class PostAdmin(admin.ModelAdmin):
    model = Article

    list_display = (
        "id",
        "title",
        "slug",
        "content"
    )
    # list_filter = (
    #     "published",
    #     "publish_date",
    # )
    list_editable = (
        "title",
        # "subtitle",
        "slug",
        "content",
    )
    search_fields = (
        "title",
        # "subtitle",
        "slug",
        # "body",
    )
    # prepopulated_fields = {
    #     "slug": (
    #         "title",
    #         "subtitle",
    #     )
    # }
    # date_hierarchy = "publish_date"
    save_on_top = True

admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    model = Author

    list_display = (
        'name'
    )