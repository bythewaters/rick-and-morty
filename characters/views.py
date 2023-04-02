import random

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from characters.models import Character
from characters.paginations import LargeResultsSetPagination
from characters.serializers import CharacterSerializer


@extend_schema(responses={status.HTTP_200_OK: CharacterSerializer})
@api_view(["GET"])
def get_random_character(request: Request) -> Response:
    """Get random character from Rick & Morty world"""
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)

    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        queryset = Character.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name", description="Filter by name", required=False, type=str
            )
        ]
    )
    def get(self, request: Request, *args, **kwargs) -> Response:
        """List characters filter by name"""
        return super().get(request, *args, **kwargs)
