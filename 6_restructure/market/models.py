from market import db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    producto = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    precio = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f'{self.producto}'