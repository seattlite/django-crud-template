from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.core import serializers
from time import mktime, gmtime, strftime
import json
import datetime

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return strftime("%a, %d %b %Y %H:%M:%S +0000", obj.timetuple())

        return json.JSONEncoder.default(self, obj)

class HybridDetailView(DetailView):
    def render_to_response(self, context):
        if self.request.is_ajax() == True:
            raw_data = serializers.serialize('python', [context['object']])
            actual_data = raw_data[0]['fields']
            return HttpResponse(
                    json.dumps(actual_data, cls = MyEncoder),
                    content_type='application/json'
                    ) 
        else:
            return super(HybridDetailView, self).render_to_response(context)

class HybridListView(ListView):
    def render_to_response(self, context):
        if self.request.is_ajax() == True:
            raw_data = serializers.serialize('python', context['object_list'])
            actual_data = [d['fields'] for d in raw_data]
            output = json.dumps(actual_data, cls = MyEncoder)
            return HttpResponse(
                    output,
                    content_type='application/json'
                    ) 
        else:
            return super(HybridListView, self).render_to_response(context)

