from django.contrib import admin

# Register your models here.
from articles.models import Articles, Author, Tag


@admin.register(Articles)
class PostAdmin(admin.ModelAdmin):
    model = Articles

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

admin.register(Articles)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author

    list_display = [
       'id', 'name'
    ]
    list_editable = (
        "name",
    )
    save_on_top = True
admin.register(Author)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

    list_display = ["id", 'name']
    list_editable = ("name",)