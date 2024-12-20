from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Painting

class DeletePaintingView(APIView):
    """
    View to delete a specific painting.
    Only the owner of the painting can delete it.
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request, painting_id):
        try:
            # Get the painting
            painting = get_object_or_404(Painting, painting_id=painting_id)
            
            # Check if the user is the owner of the painting
            if painting.artist != request.user:
                return Response(
                    {"error": "You don't have permission to delete this painting"}, 
                    status=status.HTTP_403_FORBIDDEN
                )
            
            # Delete the painting
            painting.delete()
            
            return Response(
                {"message": "Painting deleted successfully"}, 
                status=status.HTTP_200_OK
            )
            
        except Painting.DoesNotExist:
            return Response(
                {"error": "Painting not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": "Internal server error", "details": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
