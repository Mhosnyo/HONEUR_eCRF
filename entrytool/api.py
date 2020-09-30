from opal.core.api import LoginRequiredViewset
from opal.models import Patient
from opal.core.api import OPALRouter, patient_from_pk
from opal.core.views import json_response
from entrytool.episode_categories import LineOfTreatmentEpisode


class NewLineOfTreatmentEpisode(LoginRequiredViewset):
    model = Patient
    base_name = "new_line_of_treatment_episode"

    @patient_from_pk
    def update(self, request, patient):
        patient.episode_set.create(category_name=LineOfTreatmentEpisode.display_name)
        return json_response(True)


entrytool_router = OPALRouter()
entrytool_router.register(
    NewLineOfTreatmentEpisode.base_name, NewLineOfTreatmentEpisode
)