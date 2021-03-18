"""authentik Outpost administration"""
from dataclasses import asdict
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import (
    PermissionRequiredMixin as DjangoPermissionRequiredMixin,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.views.generic import UpdateView
from guardian.mixins import PermissionRequiredMixin

from authentik.lib.views import CreateAssignPermView
from authentik.outposts.forms import OutpostForm
from authentik.outposts.models import Outpost, OutpostConfig


class OutpostCreateView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    DjangoPermissionRequiredMixin,
    CreateAssignPermView,
):
    """Create new Outpost"""

    model = Outpost
    form_class = OutpostForm
    permission_required = "authentik_outposts.add_outpost"
    success_url = "/"
    template_name = "generic/create.html"
    success_message = _("Successfully created Outpost")

    def get_initial(self) -> dict[str, Any]:
        return {
            "_config": asdict(
                OutpostConfig(authentik_host=self.request.build_absolute_uri("/"))
            )
        }


class OutpostUpdateView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView,
):
    """Update outpost"""

    model = Outpost
    form_class = OutpostForm
    permission_required = "authentik_outposts.change_outpost"
    success_url = "/"
    template_name = "generic/update.html"
    success_message = _("Successfully updated Outpost")
