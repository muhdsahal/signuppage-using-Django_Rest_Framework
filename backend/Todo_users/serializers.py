from rest_framework.serializers import ModelSerializer
from .models import Users
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model =Users,
        fields = ['id','username','email','password','profile_image']
        extra_kwargs={
            'password':{'write_only':True}
        }

        def create(self,validated_data):
            password = validated_data.pop('password',None)
            instance = self.Meta.model.objects.create(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance
        
        def update(self,instance,validated_data):
            password = validated_data.get('password')
            if password:
                hashed_password = make_password(password)
                validated_data['password'] = hashed_password
            return super().update(instance,validated_data)

class myTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token =super().get_token(user)
        print(user.username,token)
        token['username']=user.username
        token['email']= user.emial
        token['is_admin'] = user.is_superuser

        return token
