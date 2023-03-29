import os
import xml.etree.ElementTree as ET
import PySimpleGUI as sg
import pandas as pd
import numpy as np

servidor_path = r"C:\Users\pablo\Desktop\NNTO"


def ler_vocacoes():
    vocacoes = {}
    xml_file = os.path.join(servidor_path, "data", "XML", "vocations.xml")
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for vocation in root.findall("vocation"):
        vocation_id = int(vocation.get("id"))
        name = vocation.get("name")
        gain_cap = int(vocation.get("gaincap"))
        gain_hp = int(vocation.get("gainhp"))
        gain_mana = int(vocation.get("gainmana"))
        gain_hp_ticks = int(vocation.get("gainhpticks"))
        gain_hp_amount = int(vocation.get("gainhpamount"))
        gain_mana_ticks = int(vocation.get("gainmanaticks"))
        gain_mana_amount = int(vocation.get("gainmanaamount"))
        mana_multiplier = float(vocation.get("manamultiplier"))
        attack_speed = float(vocation.get("attackspeed"))
        vocacoes[vocation_id] = {
            "name": name,
            "gain_cap": gain_cap,
            "gain_hp": gain_hp,
            "gain_mana": gain_mana,
            "gain_hp_ticks": gain_hp_ticks,
            "gain_hp_amount": gain_hp_amount,
            "gain_mana_ticks": gain_mana_ticks,
            "gain_mana_amount": gain_mana_amount,
            "mana_multiplier": mana_multiplier,
            "attack_speed": attack_speed,
        }
    return vocacoes

  
  def ler_feiticos():
    feiticos = {}
    xml_file = os.path.join(servidor_path, "data", "spells", "spells.xml")
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for spell in root.findall("spell"):
        spell_id = int(spell.get("id"))
        name = spell.get("name")
        words = spell.get("words")
        level = int(spell.get("lvl"))
        mana_cost = int(spell.get("mana"))
        premium = bool(int(spell.get("prem")))
        need_target = bool(int(spell.get("needtarget")))
        if need_target:
            range_ = int(spell.get("range"))
        else:
            range_ = None
        exhaustion = int(spell.get("exhaustion"))
        script = os.path.join(servidor_path, "data", "spells", "scripts", spell.get("script"))
        vocation_id = int(spell.get("vocation"))
        feiticos[spell_id] = {
            "name": name,
            "words": words,
            "level": level,
            "mana_cost": mana_cost,
            "premium": premium,
            "need_target": need_target,
            "range": range_,
            "exhaustion": exhaustion,
            "script": script,
            "vocation_id
