from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from mountains.models import Mountain, User, Coord, Level, MountainImage

from mountains.serializers import MountainSerializer


class MountainApiTestCase(APITestCase):
    def setUp(self):
        self.setup_data = Mountain.objects.create(
            title="Ural",
            user=User.objects.create(
                first_name="Ivan",
                second_name="Ivanovich",
                last_name="Ivanov",
                email="qwerty@mail.ru",
                phone="+75555555555"
            ),
            coords=Coord.objects.create(
                latitude=45.3842,
                longitude=7.1525,
                height=1200
            ),
            level=Level.objects.create(
                winter="",
                summer="1А",
                autumn="1А",
                spring=""
            )
        )
        self.image_1 = MountainImage.objects.create(
            mountain=self.setup_data,
            data="https://natworld.info/wp-content/uploads/2020/04/gora-fudzi.jpg",
            title="Intro"
        )
        self.image_2 = MountainImage.objects.create(
            mountain=self.setup_data,
            data="https://kipmu.ru/wp-content/uploads/mountain.jpg",
            title="End"
        )

        self.setup_data_status_not_new = Mountain.objects.create(
            title="Ural",
            status='PEN',
            user=User.objects.create(
                first_name="Ivan",
                second_name="Ivanovich",
                last_name="Ivanov",
                email="123456@mail.ru",
                phone="+75555555555"
            ),
            coords=Coord.objects.create(
                latitude=45.3842,
                longitude=7.1525,
                height=1200
            ),
            level=Level.objects.create(
                winter="",
                summer="1А",
                autumn="1А",
                spring=""
            )
        )
        self.image_1 = MountainImage.objects.create(
            mountain=self.setup_data,
            data="https://natworld.info/wp-content/uploads/2020/04/gora-fudzi.jpg",
            title="Intro"
        )
        self.image_2 = MountainImage.objects.create(
            mountain=self.setup_data,
            data="https://kipmu.ru/wp-content/uploads/mountain.jpg",
            title="End"
        )

    def test_get(self):
        url = reverse('submitdata-list')
        response = self.client.get(url)
        serializer_data = MountainSerializer([self.setup_data, self.setup_data_status_not_new], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        response = self.client.get(url)
        serializer_data = MountainSerializer(self.setup_data).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())

    def test_post_valid(self):
        objects_count_before = Mountain.objects.count()
        user_count_before = User.objects.count()
        new_data = {
            "title": "Ural",
            "user": {
                "first_name": "Petr",
                "second_name": "Petrovich",
                "last_name": "Petrov",
                "email": "asdfg@mail.ru",
                "phone": "+71111111111"
            },
            "coords": {
                "latitude": 45.456,
                "longitude": 65.876,
                "height": 560
            },
            "level": {
                "summer": "1А"
            },
            "images": []
        }

        url = reverse('submitdata-list')
        response = self.client.post(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(objects_count_before + 1, Mountain.objects.count())
        self.assertEqual(user_count_before + 1, User.objects.count())

    def test_post_valid_user_already_exists(self):
        objects_count_before = Mountain.objects.count()
        user_count_before = User.objects.count()
        new_data = {
            "title": "Ural",
            "user": {
                "first_name": "Ivan",
                "second_name": "Ivanovich",
                "last_name": "Ivanov",
                "email": "qwerty@mail.ru",
                "phone": "+75555555555"
            },
            "coords": {
                "latitude": 82.4864,
                "longitude": 75.7678,
                "height": 900
            },
            "level": {
                "winter": "1А"
            },
            "images": [
                {
                    "data": "https://natworld.info/wp-content/uploads/2020/04/gora-fudzi.jpg",
                    "title": "Intro"
                }
            ]
        }

        url = reverse('submitdata-list')
        response = self.client.post(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(objects_count_before + 1, Mountain.objects.count())
        self.assertEqual(user_count_before, User.objects.count())

    def test_post_invalid_user(self):
        objects_count_before = Mountain.objects.count()
        new_data = {
            "title": "Ural",
            "other_title": "Ural2",
            "user": {
                "first_name": "Ivan",
                "second_name": "Ivanovich",
                "last_name": "Ivanov",
                "phone": "+75555555555"
            },
            "coords": {
                "latitude": 45.3842,
                "longitude": 7.1525,
                "height": 1200
            },
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": ""
            },
            "images": [
                {"data": "https://natworld.info/wp-content/uploads/2020/04/gora-fudzi.jpg", "title": "Intro"},
                {"data": "https://kipmu.ru/wp-content/uploads/mountain.jpg", "title": "End"}]
        }

        url = reverse('submitdata-list')
        response = self.client.post(url, new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(objects_count_before, Mountain.objects.count())

    def test_post_invalid_coords(self):
        objects_count_before = Mountain.objects.count()
        new_data = {
            "title": "Ural",
            "other_title": "Ural2",
            "user": {
                "first_name": "Ivan",
                "second_name": "Ivanovich",
                "last_name": "Ivanov",
                "email": "qwerty@mail.ru",
                "phone": "+75555555555"
            },
            "coords": {
                "height": 1200
            },
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": ""
            },
            "images": [
                {"data": "https://natworld.info/wp-content/uploads/2020/04/gora-fudzi.jpg", "title": "Intro"},
                {"data": "https://kipmu.ru/wp-content/uploads/mountain.jpg", "title": "End"}]
        }

        url = reverse('submitdata-list')
        response = self.client.post(url, new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(objects_count_before, Mountain.objects.count())

    def test_patch_valid_title(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "title": "Kavkaz"
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.setup_data.refresh_from_db()
        self.assertEqual('Kavkaz', self.setup_data.title)

    def test_patch_valid_coords_level(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "coords": {
                "longitude": 15.6456
            },
            "level": {
                "winter": "1A"
            }
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.setup_data.refresh_from_db()
        self.assertEqual('1A', self.setup_data.level.winter)

    def test_patch_valid_add_image(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        images_count = MountainImage.objects.filter(mountain=self.setup_data).count()
        new_data = {
            "images": [
                {
                    "data": "https://natworld.info/wp-content/uploads/2020/04/gora-fudzi.jpg",
                    "title": "Седловина"
                }
            ]
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.setup_data.refresh_from_db()
        self.assertEqual(images_count + 1, MountainImage.objects.filter(mountain=self.setup_data).count())

    def test_patch_valid_update_image(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        image_id = MountainImage.objects.filter(mountain=self.setup_data).values_list('id', flat=True)[0]
        images_count = MountainImage.objects.filter(mountain=self.setup_data).count()
        new_data = {
            "images": [
                {
                    "id": image_id,
                    "data": "https://natworld.info/wp-content/uploads/2020/04/gora-fudzi.jpg",
                    "title": "Седловина"
                }
            ]
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.setup_data.refresh_from_db()
        self.assertEqual(images_count, MountainImage.objects.filter(mountain=self.setup_data).count())

    def test_patch_valid_clear_image_list(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "images": []
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.setup_data.refresh_from_db()
        self.assertEqual(0, MountainImage.objects.filter(mountain=self.setup_data).count())

    def test_patch_invalid_status(self):
        url = reverse('submitdata-detail', args=(self.setup_data_status_not_new.id,))
        new_data = {
            "title": "Kavkaz"
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_patch_invalid_user(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "user": {
                "first_name": "Pavel"
            }
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_patch_invalid_level_coords(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "level": {
                "summer": "Pavel"
            },
            "coords": {}
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, response.data.get("state"))
