from rest_framework import permissions


class AuthorOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated
                and (
                        request.user.is_admin
                        or request.user.is_superuser)
        )

    def has_object_permission(self, request, view, obj):
        return (
                obj == request.user
                or request.user.is_admin
                or request.user.is_superuser)
