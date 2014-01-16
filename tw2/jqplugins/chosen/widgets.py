import tw2.core as twc
import tw2.forms as twf
import tw2.jquery as twj

__all__ = [
    'chosen_img',
    'chosen_js',
    'chosen_css',
    'ChosenSingleSelectField',
    'ChosenMultipleSelectField']


chosen_img = twc.Link(
    modname=__name__,
    filename='static/chosen-sprite.png')
chosen_img_2x = twc.Link(
    modname=__name__,
    filename='static/chosen-sprite@2x.png')
chosen_js = twc.JSLink(
    modname=__name__,
    filename='static/chosen.jquery.js',
    resources=[twj.jquery_js],
    location='headbottom')
chosen_js_min = twc.JSLink(
    modname=__name__,
    filename='static/chosen.jquery.min.js',
    resources=[twj.jquery_js],
    location='headbottom')
chosen_css = twc.CSSLink(
    modname=__name__,
    filename='static/chosen.css')
chosen_css_min = twc.CSSLink(
    modname=__name__,
    filename='static/chosen.min.css')


class ChosenMixin(twc.Widget):
    '''Mixin for Chosen SelectFields'''
    resources = [chosen_js, chosen_css]

    selector = twc.Variable("Escaped id.  jQuery selector.")
    opts = twc.Variable(
        'Arguments for the javascript init function. '
        'See http://harvesthq.github.io/chosen/options.html',
        default=dict())

    placeholder = twc.Param(
        'Placeholder text, prompting user for selection',
        default='')
    no_results_text = twc.Param(
        'Text shown when the search term returned no results',
        default='')

    search_contains = twc.Param(
        'Allow matches starting from anywhere within a word.',
        default=False)

    def prepare(self):
        super(ChosenMixin, self).prepare()
        # put code here to run just before the widget is displayed
        if 'id' in self.attrs:
            self.selector = "#" + self.attrs['id'].replace(':', '\\:')

        if self.placeholder:
            self.attrs['data-placeholder'] = self.placeholder
        if self.no_results_text:
            self.opts['no_results_text'] = self.no_results_text
        if self.search_contains:
            self.opts['search_contains'] = True

        self.add_call(twj.jQuery(self.selector).chosen(self.opts))


class ChosenSingleSelectField(ChosenMixin, twf.SingleSelectField):
    '''SingleSelectField, enhanced with Chosen javascript'''
    def prepare(self):
        # If field is not required, this adds a button for deselection
        if not self.required:
            self.opts['allow_single_deselect'] = True
        super(ChosenSingleSelectField, self).prepare()


class ChosenMultipleSelectField(ChosenMixin, twf.MultipleSelectField):
    '''MultipleSelectField, enhanced with Chosen javascript'''
    pass
