from . import models


class Get:

    @staticmethod
    def model_list(model_sender):
        result = model_sender.objects.all().order_by('-id')
        return result

    @staticmethod
    def model_object(model_sender, pk):
        result = model_sender.objects.filter(id=pk).first()
        return result


class Change:

    @staticmethod
    def user_password(user, new_password: str):
        user.set_password(new_password)
        user.save()


class Delete:

    @staticmethod
    def model_object(model_sender, pk=None):
        result = Get.model_object(model_sender, pk)
        result.delete()


class Count:

    @staticmethod
    def cinema_count():
        return models.Cinema.objects.count()

    @staticmethod
    def cinema_hall_count():
        return models.CinemaHall.objects.count()

    @staticmethod
    def promotion_count():
        return models.Promotion.objects.count()

    @staticmethod
    def user_count():
        return models.User.objects.count()

    @staticmethod
    def news_count_gt_date(condition_date):
        return models.News.objects.filter(news_published_date__gt=condition_date).count()

    @staticmethod
    def news_count_lte_date(condition_date):
        return models.News.objects.filter(news_published_date__lte=condition_date).count()

    @staticmethod
    def film_count_gt_date(condition_date):
        return models.Film.objects.filter(first_night__gt=condition_date).count()

    @staticmethod
    def film_count_lte_date(condition_date):
        return models.Film.objects.filter(first_night__lte=condition_date).count()