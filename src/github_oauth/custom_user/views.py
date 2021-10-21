from django.contrib.auth import get_user_model
from django.views.generic import UpdateView


class UserProfileView(UpdateView):
    model = get_user_model()
    fields = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "address",
        "prev_address",
    ]
    success_url = "/myprofile"

    def get_object(self, queryset=None):
        return self.request.user
