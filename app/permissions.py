from rest_framework.permissions import BasePermission

class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        pk=view.kwargs.get('pk')
        if request.method=="GET" and request.user.is_authenticated:
            return True
        if request.method=="POST" and not request.user.is_authenticated:
            return True
        if request.method=="DELETE" and request.user.is_superuser:
            return True
        if request.method in ("PUT","PATCH") and int(pk)==request.user.id:
            return True

class GamePermissions(BasePermission):
    def has_permission(self, request, view):
        pk=view.kwargs.get('pk',None)
        if request.method=="GET" and request.user.is_authenticated:
            return True
        return False
        
class UpdateBoardPermissions(BasePermission):
    def has_permission(self, request, view):
        pk=view.kwargs.get('pk')
        if pk:
            if request.method in ("GET","PATCH") and int(pk)==request.user.id:
                return True
        else:
            if request.method in ("GET","PATCH"):
                return True
        
        
                
