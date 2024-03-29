from re import A
from rest_framework import serializers
from account.models import Account



class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['firstName', 'lastName', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    def	save(self):
        account = Account(
					firstName=self.validated_data['firstName'],
					lastName=self.validated_data['lastName'],
                    email=self.validated_data['email'],
                    password = self.validated_data['password'],
				)

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        # account.set_password(password)
        account.save()
        return account 
