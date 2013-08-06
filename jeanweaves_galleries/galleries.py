# -*- coding: utf-8 -*-


from collections import namedtuple

from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _


Photo = namedtuple('Photo', ['title', 'src_path', 'detail_src_path', 'alt', 'link_url'])


index = [
    Photo(title=_('Towels'), src_path='assets/img/towels/512/towel7.jpg', detail_src_path=None, alt=_('Towel 7'), link_url=reverse_lazy('towels')),
    Photo(title=_('Damask'), src_path='assets/img/damask/512/damask1.jpg', detail_src_path=None, alt=_('Damask 1'), link_url=reverse_lazy('damask')),
    Photo(title=_('Placemats and Napkins'), src_path='assets/img/placemats-and-napkins/512/napkins.jpg', detail_src_path=None, alt=_('Napkins'), link_url=reverse_lazy('placemats_and_napkins')),
    Photo(title=_('Runners'), src_path='assets/img/runners/512/runner2.jpg', detail_src_path=None, alt=_('Runner 2'), link_url=reverse_lazy('runners')),
    Photo(title=_('Scarves'), src_path='assets/img/scarves/512/scarf3.jpg', detail_src_path=None, alt=_('Scarf 3'), link_url=reverse_lazy('scarves')),
    Photo(title=_('Throws'), src_path='assets/img/throws/512/throw2.jpg', detail_src_path=None, alt=_('Throw 2'), link_url=reverse_lazy('throws')),
    Photo(title=_('Animals'), src_path='assets/img/animals/512/cow.jpg', detail_src_path=None, alt=_('Cow'), link_url=reverse_lazy('animals')),
]

animals = [
    Photo(title=_('Cow'), src_path='assets/img/animals/512/cow.jpg', detail_src_path=None, alt=_('Cow'), link_url=None),
    Photo(title=_('Chicken'), src_path='assets/img/animals/512/chicken.jpg', detail_src_path=None, alt=_('Chicken'), link_url=None),
    Photo(title=_('Goat'), src_path='assets/img/animals/512/goat.jpg', detail_src_path=None, alt=_('Goat'), link_url=None),
]

damask = [
    Photo(title=_("2nd Place Midwest Weavers Members' Exhibit-People of the South Wind and The Handwoven Weaving for the Home Award of Excellence"), src_path='assets/img/damask/512/damask1.jpg', detail_src_path=None, alt=_("2nd Place Midwest Weavers Members' Exhibit-People of the South Wind and The Handwoven Weaving for the Home Award of Excellence"), link_url=None),
    Photo(title=_('Damask 2'), src_path='assets/img/damask/512/damask2.jpg', detail_src_path=None, alt=_('Damask 2'), link_url=None),
    Photo(title=_('Damask 3'), src_path='assets/img/damask/512/damask3.jpg', detail_src_path=None, alt=_('Damask 3'), link_url=None),
    Photo(title=_('Damask 4'), src_path='assets/img/damask/512/damask4.jpg', detail_src_path=None, alt=_('Damask 4'), link_url=None),
    Photo(title=_('Damask 5'), src_path='assets/img/damask/512/damask5.jpg', detail_src_path=None, alt=_('Damask 5'), link_url=None),
]

placemats_and_napkins = [
    Photo(title=_('Napkin 1'), src_path='assets/img/placemats-and-napkins/512/napkin1.jpg', detail_src_path=None, alt=_('Napkin 1'), link_url=None),
    Photo(title=_('Napkins'), src_path='assets/img/placemats-and-napkins/512/napkins.jpg', detail_src_path=None, alt=_('Napkins'), link_url=None),
    Photo(title=_('Placemat'), src_path='assets/img/placemats-and-napkins/512/placemat.jpg', detail_src_path='assets/img/placemats-and-napkins/512/placemat-detail.jpg', alt=_('Placemat'), link_url=None),
    Photo(title=_('Buttercup and Blue Placemat'), src_path='assets/img/placemats-and-napkins/512/buttercup-and-blue-placemat.jpg', detail_src_path='assets/img/placemats-and-napkins/512/buttercup-and-blue-placemat-detail.jpg', alt=_('Buttercup and Blue Placemat'), link_url=None),
    Photo(title=_('Spring Green and Blue Placemat'), src_path='assets/img/placemats-and-napkins/512/spring-green-and-blue-placemat.jpg', detail_src_path='assets/img/placemats-and-napkins/512/spring-green-and-blue-placemat-detail.jpg', alt=_('Spring Green and Blue Placemat'), link_url=None),
    Photo(title=_('Summer Green and Gold Placemat'), src_path='assets/img/placemats-and-napkins/512/summer-green-and-gold-placemat.jpg', detail_src_path='assets/img/placemats-and-napkins/512/summer-green-and-gold-placemat-detail.jpg', alt=_('Summer Green and Gold Placemat'), link_url=None),
    Photo(title=_('Summer Green and Lemon Placemat'), src_path='assets/img/placemats-and-napkins/512/summer-green-and-lemon-placemat.jpg', detail_src_path='assets/img/placemats-and-napkins/512/summer-green-and-lemon-placemat-detail.jpg', alt=_('Summer Green and Lemon Placemat'), link_url=None),
    Photo(title=_('Gold Napkin'), src_path='assets/img/placemats-and-napkins/512/gold-napkin.jpg', detail_src_path='assets/img/placemats-and-napkins/512/gold-napkin-detail.jpg', alt=_('Gold Napkin'), link_url=None),
    Photo(title=_('Lemon Napkin'), src_path='assets/img/placemats-and-napkins/512/lemon-napkin.jpg', detail_src_path='assets/img/placemats-and-napkins/512/lemon-napkin-detail.jpg', alt=_('Lemon Napkin'), link_url=None),
]

runners = [
    Photo(title=_('Runner 1'), src_path='assets/img/runners/512/runner1.jpg', detail_src_path=None, alt=_('Runner 1'), link_url=None),
    Photo(title=_('Runner 2'), src_path='assets/img/runners/512/runner2.jpg', detail_src_path=None, alt=_('Runner 2'), link_url=None),
    Photo(title=_('Runner 3'), src_path='assets/img/runners/512/runner3.jpg', detail_src_path=None, alt=_('Runner 3'), link_url=None),
    Photo(title=_('Runner 4'), src_path='assets/img/runners/512/runner4.jpg', detail_src_path=None, alt=_('Runner 4'), link_url=None),
    Photo(title=_('Runner 5'), src_path='assets/img/runners/512/runner5.jpg', detail_src_path=None, alt=_('Runner 5'), link_url=None),
    Photo(title=_('Runner 6'), src_path='assets/img/runners/512/runner6.jpg', detail_src_path=None, alt=_('Runner 6'), link_url=None),
    Photo(title=_('Runner 7'), src_path='assets/img/runners/512/runner7.jpg', detail_src_path=None, alt=_('Runner 7'), link_url=None),
]

scarves = [
    Photo(title=_("Sarah's scarf"), src_path='assets/img/scarves/512/scarf-sarah.jpg', detail_src_path=None, alt=_("Sarah's scarf"), link_url=None),
    Photo(title=_('Scarf 1'), src_path='assets/img/scarves/512/scarf1.jpg', detail_src_path=None, alt=_('Scarf 1'), link_url=None),
    Photo(title=_('Scarf 2'), src_path='assets/img/scarves/512/scarf2.jpg', detail_src_path=None, alt=_('Scarf 2'), link_url=None),
    Photo(title=_('Scarf 3'), src_path='assets/img/scarves/512/scarf3.jpg', detail_src_path=None, alt=_('Scarf 3'), link_url=None),
    Photo(title=_('Scarf 4'), src_path='assets/img/scarves/512/scarf4.jpg', detail_src_path=None, alt=_('Scarf 4'), link_url=None),
    Photo(title=_('Evergreen and Navy Scarf'), src_path='assets/img/scarves/512/evergreen-and-navy-scarf.jpg', detail_src_path='assets/img/scarves/512/evergreen-and-navy-scarf-detail.jpg', alt=_('Evergreen and Navy Scarf'), link_url=None),
    Photo(title=_('Navy Variegated Scarf'), src_path='assets/img/scarves/512/navy-variegated-scarf.jpg', detail_src_path='assets/img/scarves/512/navy-variegated-scarf-detail.jpg', alt=_('Navy Variegated Scarf'), link_url=None),
]

throws = [
    Photo(title=_('Throw 1'), src_path='assets/img/throws/512/throw1.jpg', detail_src_path=None, alt=_('Throw 1'), link_url=None),
    Photo(title=_('Throw 2'), src_path='assets/img/throws/512/throw2.jpg', detail_src_path=None, alt=_('Throw 2'), link_url=None),
]

towels = [
    Photo(title=_('Towel 1'), src_path='assets/img/towels/512/towel1.jpg', detail_src_path=None, alt=_('Towel 1'), link_url=None),
    Photo(title=_('Towel 2'), src_path='assets/img/towels/512/towel2.jpg', detail_src_path=None, alt=_('Towel 2'), link_url=None),
    Photo(title=_('Towel 3'), src_path='assets/img/towels/512/towel3.jpg', detail_src_path=None, alt=_('Towel 3'), link_url=None),
    Photo(title=_('Towel 4'), src_path='assets/img/towels/512/towel4.jpg', detail_src_path=None, alt=_('Towel 4'), link_url=None),
    Photo(title=_('Towel 5'), src_path='assets/img/towels/512/towel5.jpg', detail_src_path=None, alt=_('Towel 5'), link_url=None),
    Photo(title=_('Towel 6'), src_path='assets/img/towels/512/towel6.jpg', detail_src_path=None, alt=_('Towel 6'), link_url=None),
    Photo(title=_('Towel 7'), src_path='assets/img/towels/512/towel7.jpg', detail_src_path=None, alt=_('Towel 7'), link_url=None),
    Photo(title=_('Towel 8'), src_path='assets/img/towels/512/towel8.jpg', detail_src_path=None, alt=_('Towel 8'), link_url=None),
    Photo(title=_('Towel 9'), src_path='assets/img/towels/512/towel9.jpg', detail_src_path=None, alt=_('Towel 9'), link_url=None),
    Photo(title=_('Towel 10'), src_path='assets/img/towels/512/towel10.jpg', detail_src_path=None, alt=_('Towel 10'), link_url=None),
    Photo(title=_('Towel 11'), src_path='assets/img/towels/512/towel11.jpg', detail_src_path=None, alt=_('Towel 11'), link_url=None),
    Photo(title=_('Towel 12'), src_path='assets/img/towels/512/towel12.jpg', detail_src_path=None, alt=_('Towel 12'), link_url=None),
]
