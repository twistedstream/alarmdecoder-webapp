# -*- coding: utf-8 -*-

from OpenSSL import crypto, SSL
from sqlalchemy import Column, orm

from ..extensions import db

class Setting(db.Model):
    __tablename__ = 'settings'

    id = Column(db.Integer, primary_key=True, autoincrement=True)
    name = Column(db.String(32), unique=True, nullable=False)
    int_value = Column(db.Integer)
    string_value = Column(db.String(255))

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @property
    def value(self):
        for k in ('int_value', 'string_value'):
            v = getattr(self, k)
            if v is not None:
                return v
        else:
            return None

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            self.int_value = value
            self.string_value = None
        else:
            self.string_value = str(value)
            self.int_value = None
