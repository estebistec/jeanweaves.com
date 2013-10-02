# -*- coding: utf-8 -*-


from dateutil.parser import parse
from django.conf import settings
import pytz


TIME_ZONE = pytz.timezone(settings.TIME_ZONE)


class Backend(object):

    def get_posts(self):
        return [
            {
                "date": parse("2013-09-22T19:47:25+00:00").astimezone(TIME_ZONE),
                "title": "What did you say?",
                "short_URL": "http:\/\/wp.me\/p3Wmsx-2",
                "content": u"<p>No matter what field you are in, you are sure to speak your own \u201clanguage\u201d, using terms that lose\u00a0people outside your expertise. Weaving is no different. Some weaving terms have worked their way into common idioms (Have you ever heard someone refer to \u201cthe warp and woof of life\u201d?)\u00a0but are still a little\u00a0obscure. So here\u2019s a\u00a0quick little lesson\u00a0to\u00a0help clarify\u00a0cloth-making for you!<\/p>\n<p>The place to start is the <strong><em>loom<\/em><\/strong>. The loom is the primary tool used to create cloth. There are lots of different kinds of looms: warp-weighted looms, horizontal looms, vertical looms, Navajo looms, backstrap looms, barn looms, draw looms, dobby looms, and computer-assisted looms. To learn more about all the different kinds of looms used throughout history, check out <em>The Book of Looms<\/em>by Eric Broudy (1979, University of New England). It is a thorough presentation of lots of different looms, even if it is an older book and doesn\u2019t include the more recent computer-assisted looms available now. Here\u00a0is the 12-harness Swedish draw loom that lives in my studio.<\/p>\n<p><img class=\"alignleft\" alt=\"image\" src=\"http:\/\/media.tumblr.com\/d7fb0a5ffe33074da938e564cbf2ea93\/tumblr_inline_mt2j6b3Dcm1qz4rgp.jpg\" width=\"222\" height=\"238\" \/><\/p>\n<p>The <strong><em>harnesses <\/em><\/strong>or<strong><em> shafts<\/em><\/strong> are the frames that hang inside a floor loom and carry the <strong><em>heddles <\/em><\/strong>through which the warp is threaded. There can be anywhere from 2 to 24 or more harnesses on a loom. The more harnesses one has, the more patterning is possible. Each warp thread goes through one heddle (white string heddles here) on one shaft. The exception to this is the draw loom which has two sets of harnesses and the warp will be threaded through one shaft on each set. I know\u2014it\u2019s complicated. Here you can see the front harness on my draw loom with the draw\u00a0harness hanging in the back.<\/p>\n<p><img class=\"alignleft\" alt=\"image\" src=\"http:\/\/media.tumblr.com\/c9ee0b4b28c97de93749d6d968206022\/tumblr_inline_mt2j8edad41qz4rgp.jpg\" width=\"230\" height=\"272\" \/><\/p>\n<p>The <strong><em>beater <\/em><\/strong>holds the <strong><em>reed<\/em><\/strong> which pushes the weft thread down to make the cloth. Each warp thread is threaded through one slot or <strong><em>dent <\/em><\/strong>in the reed and then through one heddle on one of the shafts. Here you can see the reed in the beater with the warp yet to be threaded on my 8-shaft loom.<\/p>\n<p>&nbsp;<\/p>\n<p>&nbsp;<\/p>\n<p>&nbsp;<\/p>\n<p><a href=\"http:\/\/jeanweaves.files.wordpress.com\/2013\/09\/header-weave.jpg\"><img class=\"size-medium wp-image-7 alignleft\" alt=\"header-weave\" src=\"http:\/\/jeanweaves.files.wordpress.com\/2013\/09\/header-weave.jpg?w=226&#038;h=300\" width=\"226\" height=\"300\" \/><\/a>More text about the header weave. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam sed condimentum lacus. Nam ut libero auctor, commodo ante eu, laoreet sem. Suspendisse sit amet egestas lacus, ut lobortis libero. Cras nec quam nulla. Maecenas tincidunt commodo posuere. Maecenas eleifend egestas metus, ut malesuada dolor euismod vel. Nulla facilisi. Ut vulputate sollicitudin lacus scelerisque feugiat. Duis sit amet rutrum mauris, vitae blandit mi.<\/p>\n",
            }
        ]
