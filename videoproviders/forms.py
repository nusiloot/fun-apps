# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _


class VideoForm(forms.Form):
    video_id = forms.CharField(max_length=255, widget=forms.HiddenInput)

    def formatted_errors(self):
        if not self.errors:
            return ""
        errors = []
        for name, field in self.fields.items():
            for error in self[name].errors:
                errors.append("<li>{}: {}</li>".format(field.label, error))

        return "<ul>" + "\n".join(errors) + "</ul>"


class SubtitleForm(VideoForm):
    # Other formats supported by Dailymotion are 'STL', 'TT', but we don't support them for now.
    uploaded_file = forms.FileField(label=_("Subtitle file (VTT or SRT without tag files only)"))
    language = forms.ChoiceField(label=_("Subtitle language"), choices=settings.SUBTITLE_SUPPORTED_LANGUAGES, initial='fr')


class ThumbnailForm(VideoForm):
    uploaded_file = forms.FileField(label=_("Thumbnail file"))
