from datetime import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DepositSerializer


@api_view(['POST'])
def deposit_calculation(request):
    """Функция расчета капитализации вклада.
    Период начисления средств - один месяц.
    Пример: Если вклад сделан 05.01.2022,
    то первое начисление произойдет 05.02.2022.
    """
    serializer = DepositSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    result = {}

    date_obj = datetime.strptime(
        serializer.validated_data.get('date'), '%d.%m.%Y'
    )

    amount = serializer.validated_data.get('amount')

    for _ in range(serializer.validated_data.get('periods')):
        procent = amount * (serializer.validated_data.get('rate') / 100) / 12
        amount += procent
        result[
            (date_obj + relativedelta(months=+_ + 1)).strftime('%d.%m.%Y')
        ] = round(amount, 2)

    return Response(result, status=status.HTTP_200_OK)
