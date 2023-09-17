from django.db import models
from django.utils import timezone
from django.db.models import CharField, DateTimeField, ForeignKey, BooleanField


class Endpoint(models.Model):
    """
    The EndPoint object represents ML API endpoint.

    Attributes:
        name: The name of the endpoint, it will be used in API URL,
        owner: The string with owner name,
        created_at: The date when endpoint was created.
    """
    name = CharField(max_length=128, verbose_name='Название роута')
    owner = CharField(max_length=128, verbose_name='Владелец')
    created_at = DateTimeField(default=timezone.now, blank=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Роут'
        verbose_name_plural = 'Роуты'

    def __str__(self):
        return self.name


class MLAlgorithm(models.Model):
    """
    The MLAlgorithm represents the ML algorithm object.

    Attributes:
        name: The name of the algorithm.
        description: The short description of how the algorithm works.
        code: The code of the algorithm.
        version: The version of the algorithm similar to software versioning.
        owner: The name of the owner.
        created_at: The date when MLAlgorithm was added.
        parent_endpoint: The reference to the Endpoint.
    """
    name = CharField(max_length=128, verbose_name='Название алгоритма')
    description = CharField(max_length=1000, verbose_name='Описание')
    code = CharField(max_length=50000, verbose_name='Код')
    version = CharField(max_length=128, verbose_name='Версия')
    owner = CharField(max_length=128, verbose_name='Владелец')
    created_at = DateTimeField(default=timezone.now, blank=True, verbose_name='Дата создания')
    parent_endpoint = ForeignKey(Endpoint, on_delete=models.CASCADE, verbose_name='Роут')

    class Meta:
        verbose_name = 'Алгоритм'
        verbose_name_plural = 'Алгоритмы'

    def __str__(self):
        return self.name


class MLAlgorithmStatus(models.Model):
    """
    The MLAlgorithmStatus represent status of the MLAlgorithm which can change during the time.

    Attributes:
        status: The status of algorithm in the endpoint. Can be: testing, staging, production, ab_testing.
        active: The boolean flag which point to currently active status.
        created_by: The name of creator.
        created_at: The date of status creation.
        parent_mlalgorithm: The reference to corresponding MLAlgorithm.

    """
    status = CharField(max_length=128, verbose_name='Статус алгоритма')
    active = BooleanField(verbose_name='Активный')
    created_by = CharField(max_length=128, verbose_name='Создан')
    created_at = DateTimeField(default=timezone.now, blank=True, verbose_name='Дата создания')
    parent_mlalgorithm = ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="status", verbose_name='Алгоритм')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return f'{self.created_by}-{self.created_at} [{self.parent_mlalgorithm}]'


class MLRequest(models.Model):
    """
    The MLRequest will keep information about all requests to ML algorithms.

    Attributes:
        input_data: The input data to ML algorithm in JSON format.
        full_response: The response of the ML algorithm.
        response: The response of the ML algorithm in JSON format.
        feedback: The feedback about the response in JSON format.
        created_at: The date when request was created.
        parent_mlalgorithm: The reference to MLAlgorithm used to compute response.
    """
    input_data = CharField(max_length=10000, verbose_name='Данные')
    full_response = CharField(max_length=10000, verbose_name='Ответ')
    response = CharField(max_length=10000, verbose_name='Ответ-JSON')
    feedback = CharField(max_length=10000, blank=True, null=True, verbose_name='Обратная связь')
    created_at = DateTimeField(default=timezone.now, blank=True, verbose_name='Дата запроса')
    parent_mlalgorithm = ForeignKey(MLAlgorithm, on_delete=models.CASCADE, verbose_name='Алгоритм')

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return f'{self.created_at} [{self.parent_mlalgorithm}]'
