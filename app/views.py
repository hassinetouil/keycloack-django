from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Your logic to fetch and return products
        import pdb;
        pdb.set_trace()
        products = {"products": ["Product1", "Product2", "Product3"]}
        return Response(products)


# or as a function-based view

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_list_view(request):
    products = {"products": ["Product1", "Product2", "Product3"]}
    return Response(products)
