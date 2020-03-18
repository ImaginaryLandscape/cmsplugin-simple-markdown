import re

from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_simple_markdown.models import SimpleMarkdownPlugin
try:
    from cms.utils import page_resolver as page  # CMS < 3.5 has 'page_resolver.get_page_from_path'
except ImportError:
    from cms.utils import page  # CMS >= 3.5 has 'page.get_page_from_path'


class SimpleMarkdownCMSPluginForm(forms.ModelForm):

    class Meta:
        model = SimpleMarkdownPlugin
        fields = '__all__'


class SimpleMarkdownCMSPlugin(CMSPluginBase):
    model = SimpleMarkdownPlugin
    name = _('Text (Markdown)')
    render_template = 'cmsplugin_simple_markdown/simple_markdown.html'
    admin_preview = False
    form = SimpleMarkdownCMSPluginForm

    def replace_links(self, markdown_text):
        def link_repl(match):
            cms_page = page.get_page_from_path(match.group(1))
            if cms_page:
                return "(" + cms_page.get_absolute_url() + ")"
            else:
                return "(#" + match.group(1) + ")"

        return re.sub(r'\(page:([^\)]+)\)', link_repl, markdown_text)

    def render(self, context, instance, placeholder):
        context['text'] = self.replace_links(instance.markdown_text)
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(SimpleMarkdownCMSPlugin)
