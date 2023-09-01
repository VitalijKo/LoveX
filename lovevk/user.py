from .utils import objects


class User:
    def __init__(self, client):
        self.client = client

    def get_info(self, target_uid, target_user_is_friend=False, referer=7, sex=2):
        data = {
            'target_uid': target_uid,
            'target_user_is_friend': target_user_is_friend,
            'referer': referer,
            'sex': sex
        }

        result = self.client.request('user/getInfo.php', _data=data)

        if not result.get('data'):
            raise Exception(result['message'])

        return objects.UserInfo(result.get('data', {})).UserInfo

    def search(self, limit_per_part=5, min_level=1, age_min=14, age_max=16, vf=False, sex=1):
        data = {
            'limit_per_part': limit_per_part,
            'min_level': min_level,
            'age_max': age_max,
            'age_min': age_min,
            'vf': vf,
            'sex': sex
        }

        result = self.client.request('user/search.php', _data=data)

        return objects.search(result.get('data')).Search

    def get_users(self, user_ids, fields='age'):
        data = {
            'uids': user_ids,
            'fields': fields
        }

        result = self.client.request('user/get.php', _data=data)

        return result

    def add_to_favorite(self, target_uid):
        data = {
            'target_uid': target_uid
        }

        result = self.client.request('user/addToFav.php', _data=data)

        return objects.Code(result).Code


    def remove_from_favorite(self, target_uid):
        data = {
            'target_uid': target_uid
        }

        result = self.client.request('user/removeFromFav.php', _data=data)

        return objects.Code(result).Code

    def update_background(self, image_url):
        data = {
            'imgUrl': image_url
        }

        result = self.client.request('user/updateBg.php', _data=data)

        return objects.Code(result).Code

    def get_stocks(self):
        result = self.client.request('user/getStocks.php', _data={})

        return result

    def update_age(self, birthdate):
        data = {
            'bdate': birthdate
        }

        result = self.client.request('user/updateAge.php', _data=data)

        return objects.Code(result).Code

    def update_region(self, country_id, region_id):
        data = {
            'country_id': country_id,
            'region_id': region_id
        }

        result = self.client.request('user/updateRegion.php', _data=data)

        return result

    def change_status(self, text):
        data = {
            'text': text
        }

        result = self.client.request('user/changeStatus.php', type='post', _data=data)

        return objects.Code(result).Code

    def buy_invisible(self, period_index):
        data = {
            'period_index': period_index
        }

        result = self.client.request('user/buyInvisible.php', _data=data)

        return objects.Code(result).Code

    def extend_invisible(self):
        result = self.client.request('user/extendInvisible.php', _data={})

        return objects.Code(result).Code

    def get_text_colors_and_ratings(self, user_ids):
        data = {
            'uids': user_ids
        }

        result = self.client.request('user/getTextColorsAndRatings.php', _data=data)

        return result

    def get_top_list(self, all=True):
        result = self.client.request('user/top.php', _data={'all': all})

        return objects.top(result.get('data', {})).Top

    def inc_balance(self, action_id=6):
        result = self.client.request('user/incBalance.php', _data={'action_id': action_id})

        return objects.Code(result).Code

    def get_self_balance(self):
        result = self.client.request('user/getSelfBalance.php')

        return objects.Balance(result).Balance

    def on_group_subscribe(self):
        result = self.client.request('user/onGroupSubscribe.php')

        return objects.Code(result).Code

    def check_warns(self):
        result = self.client.request('user/checkWarns.php')

        return objects.warns(result).Warns

    def user_secret_name_inc_wall_posts(self):
        result = self.client.request('user/secretName/incWallPosts.php')

        return objects.Code(result).Code

    def buy_emoji_subscribe(self, price=10):
        data = {
            'price': price
        }

        result = self.client.request('user/buyEmojiSubscribe.php', _data=data)

        return result

    def complaint(self, type, user_id):
        data = {
            'type': type,
            'uid': user_id
        }

        result = self.client.request('user/complaint.php', _data=data)

        return result
