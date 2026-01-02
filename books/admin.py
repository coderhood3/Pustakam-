from django.contrib import admin
from .models import Category, Book, Review, Order, OrderItem, Cart

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="height: 50px;">'
        return "-"
    image_preview.allow_tags = True

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'price', 'status', 'created_at')
    list_filter = ('status', 'condition', 'category')
    search_fields = ('title', 'author', 'seller__username')
    actions = ['approve_books', 'reject_books']

    def approve_books(self, request, queryset):
        queryset.update(status='Approved')
    approve_books.short_description = "Approve selected books"

    def reject_books(self, request, queryset):
        queryset.update(status='Rejected')
    reject_books.short_description = "Reject selected books"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'full_name')

admin.site.register(Review)
admin.site.register(Cart)
