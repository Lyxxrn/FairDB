from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Manufacturer, Score, Certification, UserReview
from .serializers import ProductSerializer, ManufacturerSerializer, ScoreSerializer, CertificationSerializer, UserReviewSerializer

class ProductView(APIView):
    def post(self, request):
        # Create or update Manufacturer
        manufacturer_data = request.data.get('manufacturer')
        manufacturer_serializer = ManufacturerSerializer(data=manufacturer_data)
        if manufacturer_serializer.is_valid():
            manufacturer = manufacturer_serializer.save()
        else:
            return Response(manufacturer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create or update Product
        product_data = request.data.get('product')
        product_data['manufacturer'] = manufacturer.id
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product = product_serializer.save()
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create or update Score
        score_data = request.data.get('score')
        score_data['product'] = product.id
        score_serializer = ScoreSerializer(data=score_data)
        if score_serializer.is_valid():
            score_serializer.save()
        else:
            return Response(score_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create or update Certification
        certification_data = request.data.get('certification')
        certification_data['product'] = product.id
        certification_serializer = CertificationSerializer(data=certification_data)
        if certification_serializer.is_valid():
            certification_serializer.save()
        else:
            return Response(certification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(product_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update Manufacturer
        manufacturer_data = request.data.get('manufacturer')
        manufacturer_serializer = ManufacturerSerializer(product.manufacturer, data=manufacturer_data)
        if manufacturer_serializer.is_valid():
            manufacturer_serializer.save()
        else:
            return Response(manufacturer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update Product
        product_data = request.data.get('product')
        product_data['manufacturer'] = product.manufacturer.id
        product_serializer = ProductSerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update Score
        score_data = request.data.get('score')
        score = Score.objects.get(product=product)
        score_serializer = ScoreSerializer(score, data=score_data)
        if score_serializer.is_valid():
            score_serializer.save()
        else:
            return Response(score_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update Certification
        certification_data = request.data.get('certification')
        certification = Certification.objects.get(product=product)
        certification_serializer = CertificationSerializer(certification, data=certification_data)
        if certification_serializer.is_valid():
            certification_serializer.save()
        else:
            return Response(certification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update UserReview
        user_review_data = request.data.get('user_review')
        user_review = UserReview.objects.get(product=product)
        user_review_serializer = UserReviewSerializer(user_review, data=user_review_data)
        if user_review_serializer.is_valid():
            user_review_serializer.save()
        else:
            return Response(user_review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(product_serializer.data, status=status.HTTP_200_OK)

class UserReviewListCreateView(generics.ListCreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer

class UserReviewDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer

class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        key = self.request.query_params.get('key')
        if key:
            return Product.objects.filter(key=key)
        return Product.objects.all()