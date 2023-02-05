from datetime import datetime

from rest_framework import serializers

from .models import Deposit


class DepositSerializer(serializers.ModelSerializer):
    def validate(self, data):
        date = data.get('date')

        try:
            date_obj = datetime.strptime(date, '%d.%m.%Y')
        except ValueError:
            raise serializers.ValidationError(
                'Введенная дата не корректна'
            )
        else:
            del date_obj

        period = data.get('periods')

        if not 1 <= period <= 60:
            raise serializers.ValidationError(
                'Период вклада может быть от 1 до 60 месяцев'
            )

        amount = data.get('amount')

        if not 10000 <= amount <= 3000000:
            raise serializers.ValidationError(
                'Вклад может быть от 10000 до 3000000'
            )

        return data

    class Meta:
        model = Deposit
        fields = ('date', 'periods', 'amount', 'rate')
