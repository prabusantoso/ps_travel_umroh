# -*- coding: utf-8 -*-
from odoo import models, fields, api

class res_partner (models.Model):
    _inherit = "res.partner"

    no_identitas = fields.Char(string="No KTP")
    nama_ayah = fields.Char(string="Nama Ayah")
    nama_ibu = fields.Char(string="Nama Ibu")
    tempat_lahir = fields.Char(string="Tempat Lahir")
    tanggal_lahir = fields.Char(string="Tanggal Lahir")
    gol_darah = fields.Selection([
        ("a","A"),
        ("b","B"),
        ("ab","AB"),
        ("o","O")], string="Golongan Darah")
    jenis_kelamin = fields.Selection([
        ("pria","Pria"),
        ("wanita","Wanita")], string="Jenis Kelamin")
    status_pernikahan = fields.Selection([
        ("belum","Single"),
        ("nikah","Menikah"),
        ("cerai","Pisah")], string="Status Pernikahan")
