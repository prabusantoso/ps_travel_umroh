# -*- coding: utf-8 -*-
from odoo import models, fields, api

# class ps_travel_umroh(models.Model):
#     _name = 'ps_travel_umroh.ps_travel_umroh'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class paket_perjalanan(models.Model):
    _name = "paket.perjalanan"

    name = fields.Char(string='Reference', readonly=True, default='/')
    product_id = fields.Many2one('product.product', string="Product", required ="True")
    tgl_berangkat = fields.Date(string="Tanggal Keberangkatan", requied=True)
    tgl_pulang = fields.Date(string="Tanggal Kembali / Pulang", requied=True)
    quota = fields.Integer(string="Quota")
    quota_progress = fields.Float(string="Quota Progress", compute="_taken_seats")
    note = fields.Text(string="Notes")
    hotel_line = fields.One2many("paket.hotel.line", "paket_hotel_id", string="Hotel Lines")
    pesawat_line = fields.One2many("paket.pesawat.line", "paket_pesawat_id", string="Airline Lines")
    acara_line = fields.One2many("paket.acara.line", "paket_acara_id", string="Schedule Lines")
    peserta_line = fields.One2many("paket.peserta.line", "paket_peserta_id", string="Jamaah Lines", readonly=True)

    @api.model
    def create(self,vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('paket.perjalanan')
        return super(paket_perjalanan,self).create(vals)

    @api.multi
    def name_get(self):
        return [(this.id, this.name + "#" + " " + this.product_id.partner_ref) for this in self]

    @api.depends('quota', 'peserta_line')
    def _taken_seats(self):
        for total in self:
            if not total.quota:
                total.quota_progress = 0.0
            else:
                total.quota_progress = 100.0 * len(total.peserta_line) / total.quota
 

class paket_hotel_line(models.Model):
    _name = "paket.hotel.line"

    paket_hotel_id = fields.Many2one('paket.perjalanan', string='Paket Perjalanan', ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='Hotel', required=True)
    tgl_awal = fields.Date(string='Start Date', required=True)
    tgl_akhir = fields.Date(string='End Date', required=True)
    kota = fields.Char(related='partner_id.city', string='City', readonly=True)

    
class paket_pesawat_line(models.Model):
    _name = "paket.pesawat.line"

    paket_pesawat_id = fields.Many2one('paket.perjalanan', string='Paket Perjalanan', ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='Airlines', required=True)
    tgl_berangkat = fields.Date(string='Depature Date', required=True)
    kota_asal = fields.Char(string='Depature City', requied=True)
    kota_tujuan = fields.Char('Arrival City', required=True)


class paket_acara_line(models.Model):
    _name = "paket.acara.line"

    paket_acara_id = fields.Many2one('paket.perjalanan', string='Paket Perjalanan', ondelete='cascade')
    name = fields.Char(string='Name', required=True)
    tgl = fields.Date(string='Date', required=True)

class paket_peserta_line(models.Model):
    _name = "paket.peserta.line"

    paket_peserta_id = fields.Many2one('paket.perjalanan', string='Paket Perjalanan', ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='Jamaah')