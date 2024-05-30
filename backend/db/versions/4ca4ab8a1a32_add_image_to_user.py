"""add image to user

Revision ID: 4ca4ab8a1a32
Revises: 39c4e44aa237
Create Date: 2024-05-30 17:16:55.726684

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "4ca4ab8a1a32"
down_revision = "39c4e44aa237"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("image", sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "image")
    # ### end Alembic commands ###
