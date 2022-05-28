from rest_framework import serializers
from .models import Csat_filtred_phones
from rest_framework.exceptions import ValidationError

class FiltredPhonesSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=15)
    def validate_phone(self, value):
        if self.instance and self.instance.phone != value:
            raise ValidationError("You may not edit phone")
        return value

    created_by = serializers.CharField(max_length=30)
    def validate_created_by(self, value):
        if self.instance and self.instance.created_by != value:
            raise ValidationError("You may not edit created_by")
        return value

    creation_reason = serializers.CharField(max_length=255)

    def validate_created_reason(self, value):
        if self.instance and self.instance.creation_reason != value:
            raise ValidationError("You may not edit creation_reason")
        return value

    is_deactivated = serializers.BooleanField()

    def validate_is_deactivated(self, value):
        if self.instance and self.instance.is_deactivated == True:
            raise ValidationError("Deactivated phones can't be edited")
        return value

    class Meta:
        model = Csat_filtred_phones
        fields = ('id', 'phone', 'created_by', 'created_at', 'creation_reason', 'is_deactivated', 'deactivated_by', 'deactivated_at', 'deactivation_reason')
