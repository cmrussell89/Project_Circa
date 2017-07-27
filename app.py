from flask import Flask, render_template, redirect, url_for, flash
import requests
from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField


app = Flask(__name__)
app.config['SECRET_KEY'] = "565&SDdsa7fgSdst7%6"

#: Set Choices For Each Building //

B100_Enc_Dec = [('10.203.81.151', '608 Decoder'), ('10.203.81.152', '601 Decoder'), ('10.203.81.153', 'ALC1 Decoder'),
                ('10.203.81.154', 'ALC2 Decoder'), ('10.203.81.155', 'ALC3 Decoder')]
B100_Net = [('10.203.81.156', 'Net Relay 1'), ('10.203.81.157', 'Net Relay 2'), ('10.203.81.158', 'Net Relay 3')]
B200_Enc_Dec = [('10.202.91.220', 'ALC1 Encoder'), ('10.202.91.221', 'ALC2 Encoder'), ('10.202.91.222', 'ALC3 Encoder')]
B200_Net = [('10.202.91.223', 'ALC1 Net Relay 1')]
B201N_Enc_Dec = [('10.202.94.225', '608 Decoder'), ('10.202.94.226', '601 Decoder'), ('10.202.94.227', 'ALC1 Decoder')]
B201N_Net = [('10.202.94.228', 'Net Relay 1'), ('10.202.94.229', 'Net Relay 2')]
B201S_Enc_Dec = [('10.202.95.216', '608 Decoder'), ('10.202.95.217', '601 Decoder'), ('10.202.95.218', 'ALC1 Decoder')]
B201S_Net = [('10.202.95.219', 'Net Relay 1'), ('10.202.95.220', 'Net Relay 2')]
B400_Enc_Dec = [('10.202.145.214', '608 Decoder'), ('10.202.145.215', '601 Decoder'), ('10.202.145.216', 'ALC1 Decoder'),
                ('10.202.145.217', 'ALC2 Decoder'), ('10.202.145.218', 'ALC3 Decoder'),
                ('10.202.142.238', '400A Encoder')]
B400_Net = [('10.202.145.220', 'Net Relay 1'), ('10.202.145.221', 'Net Relay 2'), ('10.202.142.239', '400A Net Relay 1')]
B400A_Enc_Dec = [('10.203.168.226', '608 Decoder'), ('10.203.168.227', '601 Decoder'), ('10.203.168.228', 'ALC1 Decoder'),
                 ('10.203.168.229', 'ALC2 Decoder'), ('10.203.168.230', 'ALC3 Decoder')]
B400A_Net = [('10.203.168.231', 'Net Relay 1'), ('10.203.168.232', 'Net Relay 2')]
B501_Enc_Dec = [('10.203.233.184', '608 Decoder'), ('10.203.233.185', '601 Decoder')]
B501_Net = [('10.203.233.186', 'Net Relay 1')]
B601_Enc_Dec = [('10.202.20.154', '601 Encoder'),  ('10.202.20.156', '608 Decoder')]
B601_Net = [('10.202.20.155', 'Net Relay 1')]
B602_Enc_Dec = [('10.203.235.227', '608 Decoder'), ('10.203.235.223', '601 Decoder')]
B602_Net = [('10.203.235.224', 'Net Relay 1')]
B603_Enc_Dec = [('10.203.230.209', '608 Decoder'), ('10.203.230.210', '601 Decoder')]
B603_Net = [('10.203.230.211', 'Net Relay 1')]
B606_Enc_Dec = [('10.203.224.216', '608 Decoder'), ('10.203.224.217', '601 Decoder')]
B606_Net = [('10.203.224.218', 'Net Relay 1')]
B608_Enc_Dec = [('10.202.175.232', '608 Encoder')]
B608_Net = [('10.202.175.233', 'Net Relay 1'), ('10.202.175.234', 'Net Relay 2'), ('10.202.175.235', 'Net Relay 3'),
            ('10.202.175.236', 'Net Relay 4'), ('10.202.175.237', 'Net Relay 5')]
B611_Enc_Dec = [('10.203.220.233', '608 Decoder'), ('10.203.220.234', '601 Decoder')]
B611_Net = [('10.203.220.235', 'Net Relay 1')]
B800_Enc_Dec = [('10.202.230.155', '608 Decoder'), ('10.202.230.181', '601 Decoder'), ('10.202.230.157', 'ALC1 Decoder'),
                ('10.202.230.158', 'ALC2 Decoder'), ('10.202.230.159', 'ALC3 Decoder')]
B800_Net = [('10.202.230.160', 'Net Relay 1'), ('10.202.230.161', 'Net Relay 2')]
B2000S_Enc_Dec = [('10.202.171.224', '608 Decoder'), ('10.202.171.225', '601 Decoder'), ('10.202.171.226', 'ALC1 Decoder'),
                 ('ALC2 IP', 'ALC2 Decoder (No IP)'), ('ALC3 IP', 'ALC3 Decoder (No IP)')]
B2000S_Net = [('10.202.171.227', 'Net relay 1'), ('10.202.171.228', 'Net Relay 2')]
B2000N_Enc_Dec = [('10.202.171.218', '608 Decoder'), ('10.202.171.219', '601 Decoder'), ('10.202.171.220', 'ALC1 Decoder'),
                  ('10.202.171.221', 'ALC2 Decoder')]
B2000N_Net = [('10.202.171.222', 'Net Relay 1'), ('10.202.171.223', 'Net Relay 2')]
B2kA_Enc_Dec = [('10.202.179.218', '608 Decoder'), ('10.202.179.219', '601 Decoder'), ('10.202.179.220', 'ALC1 Decoder'),
                ('10.202.179.221', 'ALC2 Decoder'), ('10.202.179.222', 'ALC3 Decoder')]
B2kA_Net = [('10.202.179.223', 'Net Relay 1'), ('10.202.179.224', 'Net Relay 2')]
B3000ASL_Enc_Dec = [('10.203.190.216', '608 Decoder'), ('10.203.190.217', '601 Decoder'), ('10.203.190.218', 'ALC3 Decoder')]
B3000ASL_Net = [('10.203.190.220', 'Net Relay 1'), ('10.203.190.221', 'Net Relay 2')]
B3000ANL_Enc_Dec = [('10.203.192.227', '608 Decoder'), ('10.203.192.228', '601 Decoder'), ('10.203.192.229', 'ALC3 Decoder')]
B3000ANL_Net = [('10.203.192.231', 'Net Relay 1'), ('10.203.192.232', 'Net Relay 2')]
Childcare_Enc_Dec = [('10.202.214.186', '608 Decoder'), ('10.202.214.187', '601 Decoder')]
Childcare_Net = [('10.202.214.188', 'Net Relay 1')]
TMS_Enc_Dec = [('10.202.214.191', '608 Decoder'), ('10.202.214.192', '601 Decoder')]
TMS_Net = [('10.202.214.193', 'Net Relay 1')]
Fit_Enc_Dec = [('10.202.214.196', '608 Decoder'), ('10.202.214.197', '601 Decoder')]
Fit_Net = [('10.202.214.198', 'Net Relay 1')]


class RebootForm(FlaskForm):
    B100_Enc_Dec = SelectMultipleField('Building 100 Encoders / Decoders', choices=B100_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B100_Net = SelectMultipleField('Building 100 Net Relays', choices=B100_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B200_Enc_Dec = SelectMultipleField('Building 200 Encoders / Decoders', choices=B200_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B200_Net = SelectMultipleField('Building 200 Net Relays', choices=B200_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B201N_Enc_Dec = SelectMultipleField('Building 201 N Encoders / Decoders', choices=B201N_Enc_Dec,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False))
    B201N_Net = SelectMultipleField('Building 201 Net Relays', choices=B201N_Net,
                                    option_widget=widgets.CheckboxInput(),
                                    widget=widgets.ListWidget(prefix_label=False))
    B201S_Enc_Dec = SelectMultipleField('Building 201 S Encoders / Decoders', choices=B201S_Enc_Dec,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False))
    B201S_Net = SelectMultipleField('Building 201 S Net Relays', choices=B201S_Net,
                                    option_widget=widgets.CheckboxInput(),
                                    widget=widgets.ListWidget(prefix_label=False))
    B400_Enc_Dec = SelectMultipleField('Building 400 Encoders / Decoders', choices=B400_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B400_Net = SelectMultipleField('Building 400 Net Relays', choices=B400_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B400A_Enc_Dec = SelectMultipleField('Building 400 Add. Encoders / Decoders', choices=B400A_Enc_Dec,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False))
    B400A_Net = SelectMultipleField('Building 400 Add. Net Relays', choices=B400A_Net,
                                    option_widget=widgets.CheckboxInput(),
                                    widget=widgets.ListWidget(prefix_label=False))
    B501_Enc_Dec = SelectMultipleField('Building 501 Encoders / Decoders', choices=B501_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B501_Net = SelectMultipleField('Building 501 Net Relays', choices=B501_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B601_Enc_Dec = SelectMultipleField('Building 601 Encoders / Decoders', choices=B601_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B601_Net = SelectMultipleField('Building 601 Net Relays', choices=B601_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B602_Enc_Dec = SelectMultipleField('Building 602 Encoders / Decoders', choices=B602_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B602_Net = SelectMultipleField('Building 602 Net Relays', choices=B602_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B603_Enc_Dec = SelectMultipleField('Building 603 Encoders / Decoders', choices=B603_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B603_Net = SelectMultipleField('Building 603 Net Relays', choices=B603_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B606_Enc_Dec = SelectMultipleField('Building 606 Encoders / Decoders', choices=B606_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B606_Net = SelectMultipleField('Building 606 Net Relays', choices=B606_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B608_Enc_Dec = SelectMultipleField('Building 608 Encoders / Decoders', choices=B608_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B608_Net = SelectMultipleField('Building 608 Net Relays', choices=B608_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B611_Enc_Dec = SelectMultipleField('Building 611 Encoders / Decoders', choices=B611_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B611_Net = SelectMultipleField('Building 611 Net Relays', choices=B611_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B800_Enc_Dec = SelectMultipleField('Building 800 Encoders / Decoders', choices=B800_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B800_Net = SelectMultipleField('Building 800 Net Relays', choices=B800_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B2000S_Enc_Dec = SelectMultipleField('Building 2000 S Encoders / Decoders', choices=B2000S_Enc_Dec,
                                         option_widget=widgets.CheckboxInput(),
                                         widget=widgets.ListWidget(prefix_label=False))
    B2000S_Net = SelectMultipleField('Building 2000 S Net Relays', choices=B2000S_Net,
                                     option_widget=widgets.CheckboxInput(),
                                     widget=widgets.ListWidget(prefix_label=False))
    B2000N_Enc_Dec = SelectMultipleField('Building 2000 N Encoders / Decoders', choices=B2000N_Enc_Dec,
                                         option_widget=widgets.CheckboxInput(),
                                         widget=widgets.ListWidget(prefix_label=False))
    B2000N_Net = SelectMultipleField('Building 2000 N Net Relays', choices=B2000N_Net,
                                     option_widget=widgets.CheckboxInput(),
                                     widget=widgets.ListWidget(prefix_label=False))
    B2kA_Enc_Dec = SelectMultipleField('Building 2000 Add. Encoders / Decoders', choices=B2kA_Enc_Dec,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B2kA_Net = SelectMultipleField('Building 2000 Add. Net Relays', choices=B2kA_Net,
                                   option_widget=widgets.CheckboxInput(),
                                   widget=widgets.ListWidget(prefix_label=False))
    B3000ASL_Enc_Dec = SelectMultipleField('Building 3000 A-S Lexus Encoders /Decoders', choices=B3000ASL_Enc_Dec,
                                           option_widget=widgets.CheckboxInput(),
                                           widget=widgets.ListWidget(prefix_label=False))
    B3000ASL_Net = SelectMultipleField('Building 3000 A-S Lexus Net Relays', choices=B3000ASL_Net,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    B3000ANL_Enc_Dec = SelectMultipleField('Building 3000 A-N Lexus', choices=B3000ANL_Enc_Dec,
                                           option_widget=widgets.CheckboxInput(),
                                           widget=widgets.ListWidget(prefix_label=False))
    B3000ANL_Net = SelectMultipleField('Building 3000 A-N Lexus', choices=B3000ANL_Net,
                                       option_widget=widgets.CheckboxInput(),
                                       widget=widgets.ListWidget(prefix_label=False))
    Childcare_Enc_Dec = SelectMultipleField('Childcare Encoders / Decoders', choices=Childcare_Enc_Dec,
                                            option_widget=widgets.CheckboxInput(),
                                            widget=widgets.ListWidget(prefix_label=False))
    Childcare_Net = SelectMultipleField('Childcare Net relays', choices=Childcare_Net,
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False))
    TMS_Enc_Dec = SelectMultipleField('Team Member Services Encoders / Decoders', choices=TMS_Enc_Dec,
                                      option_widget=widgets.CheckboxInput(),
                                      widget=widgets.ListWidget(prefix_label=False))
    TMS_Net = SelectMultipleField('Team Member Services Net Relays', choices=TMS_Net,
                                  option_widget=widgets.CheckboxInput(),
                                  widget=widgets.ListWidget(prefix_label=False))
    Fit_Enc_Dec = SelectMultipleField('Fitness Center Encoders / Decoders', choices=Fit_Enc_Dec,
                                      option_widget=widgets.CheckboxInput(),
                                      widget=widgets.ListWidget(prefix_label=False))
    Fit_Net = SelectMultipleField('Fitness Center Net Relays', choices=Fit_Net,
                                  option_widget=widgets.CheckboxInput(),
                                  widget=widgets.ListWidget(prefix_label=False))


@app.route('/')
def index():
    return redirect(url_for('form'))


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = RebootForm()
    if form.validate_on_submit():
        ip_addresses = (form.B100_Enc_Dec.data + form.B200_Enc_Dec.data + form.B201N_Enc_Dec.data + form.B201S_Enc_Dec.data +
                        form.B400_Enc_Dec.data + form.B400A_Enc_Dec.data + form.B501_Enc_Dec.data + form.B601_Enc_Dec.data +
                        form.B602_Enc_Dec.data + form.B603_Enc_Dec.data + form.B606_Enc_Dec.data +
                        form.B608_Enc_Dec.data + form.B611_Enc_Dec.data + form.B800_Enc_Dec.data +
                        form.B2000S_Enc_Dec.data + form.B2000N_Enc_Dec.data + form.B2kA_Enc_Dec.data +
                        form.B3000ANL_Enc_Dec.data + form.B3000ASL_Enc_Dec.data + form.Childcare_Enc_Dec.data +
                        form.TMS_Enc_Dec.data + form.Fit_Enc_Dec.data)
        for ip_address in ip_addresses:
            try:
                requests.get('http://{}/rc.cgi?L=uirreboot.html&c=99'.format(ip_address))
                flash('rebooting {}'.format(ip_address))
            except Exception:
                flash('{} did not reboot. It may be offline.'.format(ip_address), 'error')
        ip_addresses_nr = (form.B100_Net.data + form.B200_Net.data + form.B201N_Net.data + form.B201S_Net.data +
                           form.B400_Net.data + form.B400A_Net.data + form.B501_Net.data + form.B601_Net.data +
                           form.B602_Net.data + form.B603_Net.data + form.B606_Net.data + form.B608_Net.data +
                           form.B611_Net.data + form.B800_Net.data + form.B2000S_Net.data + form.B2000N_Net.data +
                           form.B2kA_Net.data + form.B3000ANL_Net.data + form.B3000ASL_Net.data +
                           form.Childcare_Net.data + form.TMS_Net.data + form.Fit_Net.data)
        for ip_address_nr in ip_addresses_nr:
            try:
                requests.get('http://{}/setup.cgi?L=uireboot2.html&R'.format(ip_address_nr))
                flash('rebooting {}'.format(ip_address_nr))
            except Exception:
                flash('{} did not reboot. It may be offline.'.format(ip_address_nr), 'error')
        return redirect(url_for('form'))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

