# -*- coding: utf-8 -*-
class GildedRose(object):
  def __init__(self, items):
    self.items = [ItemFactory.get_item_decorator(item) for item in items]

  def update_quality(self):
    for item in self.items:
      item.update_item()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemDecorator:
  def __init__(self, item):
    self.item = item

  def update_quality(self):
    raise NotImplementedError("Please Implement this method")

  def update_sell_in(self):
    self.item.sell_in = self.item.sell_in - 1

  def update_item(self):
    self.update_quality()
    self.update_sell_in()

class RegularItemDecorator(ItemDecorator):
  def update_quality(self):
    updated_quality = self.item.quality
    if self.item.sell_in > 0:
      updated_quality = updated_quality - 1
    else:
      updated_quality = updated_quality - 2
    updated_quality = max(0, updated_quality)
    self.item.quality = updated_quality

class AgedBrieItemDecorator(ItemDecorator):
  def update_quality(self):
    self.item.quality = min(50, self.item.quality + 1)

class SulfurasItemDecorator(ItemDecorator):
  def update_quality(self):
    return

  def update_sell_in(self):
    return

class BackstageItemDecorator(ItemDecorator):
  def update_quality(self):
    if self.item.sell_in > 10:
      self.item.quality = self.item.quality + 1
    elif self.item.sell_in > 5:
      self.item.quality = self.item.quality + 2
    elif self.item.sell_in > 0:
      self.item.quality = self.item.quality + 3
    else:
      self.item.quality = 0

class ConjuredItemDecorator(ItemDecorator):
  def update_quality(self):
    updated_quality = self.item.quality
    if self.item.sell_in > 0:
      updated_quality = updated_quality - 2
    else:
      updated_quality = updated_quality - 4
    updated_quality = max(0, updated_quality)
    self.item.quality = updated_quality

class ItemFactory:
  def get_item_decorator(item):
    if item.name.startswith('Aged Brie'):
      return AgedBrieItemDecorator(item)
    elif item.name.startswith('Sulfuras'):
      return SulfurasItemDecorator(item)
    elif item.name.startswith('Backstage'):
      return BackstageItemDecorator(item)
    elif item.name.startswith('Conjured'):
      return ConjuredItemDecorator(item)
    else:
      return RegularItemDecorator(item)