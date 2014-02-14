# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from flask.ext.wtf.html5 import URLField, EmailField, TelField
from wtforms import (ValidationError, HiddenField, TextField, HiddenField,
        PasswordField, SubmitField, TextAreaField, IntegerField, RadioField,
        FileField, DecimalField, SelectField, BooleanField, SelectMultipleField)
from wtforms.validators import (Required, Length, EqualTo, Email, NumberRange,
        URL, AnyOf, Optional)
from wtforms.widgets import ListWidget, CheckboxInput
from ..settings.forms import NetworkDeviceForm, SerialDeviceForm
from ..settings.constants import NETWORK_DEVICE, SERIAL_DEVICE

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class DeviceTypeForm(Form):
    device_type = SelectField(u'Device Type', choices=[('AD2USB', u'AD2USB'), ('AD2PI', u'AD2PI'), ('AD2SERIAL', u'AD2SERIAL')], default='AD2USB')

    submit = SubmitField(u'Next')

class DeviceLocationForm(Form):
    device_location = SelectField(u'Device Location', choices=[('local', 'Local Device'), ('network', 'Network')], default='local')

    submit = SubmitField(u'Next')

class SSLForm(Form):
    cert = FileField(u'Certificate')

    submit = SubmitField(u'Next')

class SSLHostForm(Form):
    host = BooleanField(u'Would you like us to make the device available over your network?')

    submit = SubmitField(u'Next')

class DeviceForm(Form):
    device_address = TextField(u'Keypad Address', [Required()])
    address_mask = TextField(u'Address Mask', [Required(), Length(max=8)])
    lrr_enabled = BooleanField(u'Emulate Long Range Radio?')
    zone_expanders = MultiCheckboxField(u'Zone expanders', choices=['#1', '#2', '#3', '#4', '#5'])
    relay_expanders = MultiCheckboxField(u'Relay expanders', choices=['#1', '#2', '#3', '#4', '#5'])
    deduplicate = BooleanField(u'Deduplicate messages?')

    submit = SubmitField(u'Next')