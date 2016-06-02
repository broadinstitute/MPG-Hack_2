from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('dna', VARCHAR(length=64)),
    Column('rna', VARCHAR(length=120)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('protocol_description', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['dna'].drop()
    pre_meta.tables['user'].columns['rna'].drop()
    post_meta.tables['user'].columns['protocol_description'].create()
    post_meta.tables['user'].columns['title'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['dna'].create()
    pre_meta.tables['user'].columns['rna'].create()
    post_meta.tables['user'].columns['protocol_description'].drop()
    post_meta.tables['user'].columns['title'].drop()
