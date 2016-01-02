
import json

from django.http import HttpResponse
from django.views.generic import View

from app.models import Node
from app.utils import unzip_data
from app.utils import trending


class GraphView(View):

    def get(self, request):
        livetvusername = request.user.userprofile.livetvusername
        dataX, dataY, siteY = unzip_data(Node.objects.get_plottable_eight_minutes(livetvusername))
        last_node = Node.objects.filter(livetvusername=livetvusername).last()
        current_count = 0
        if last_node:
            current_count = last_node.current_total
        context = {"trending": trending(dataY),
                   "frontpaged": request.user.userprofile.frontpaged,
                   "maxY": max(dataY),
                   "maxSiteY": max(siteY),
                   "dataX": dataX,
                   "dataY": dataY,
                   "siteY": siteY,
                   "current_count": current_count}
        return HttpResponse(json.dumps(context), content_type="application/json")
