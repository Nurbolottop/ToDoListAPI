#rest
from rest_framework import serializers

#my imports
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ('id','username','email',
                  'phone_number','created_at','age')
        
class UserDetail(serializers.ModelSerializer):
    # user_posts = CardSerializers(read_only = True, many = True)
    class Meta:
        model = User
        fields = ('id','username','email',
                  'phone_number','created_at','age')
        
class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length = 255, write_only = True
    )
    password2 = serializers.CharField(
        max_length = 255, write_only = True
    )
    
    class Meta:
        model = User
        fields = ('id','username','email',
                  'phone_number','created_at','age',
                 'password','password2'
                 )
        
    def validate(self, attrs):
        if attrs['password'] !=attrs['password2']:
            raise serializers.ValidationError({'password': 'Пароли отличаются'})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({"phone_number": "Напишите номер с +996"})
        return super().validate(attrs)
    
    def create(self,values):
        user = User.objects.create(
            username = values['username'],first_name = ['values'],
            last_name = values['last_name'], email = values['email'],bio = values['bio']
        )
        user.set_password(values['password'])
        user.save()
        return user