from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Counter:

    def __init__(self, total):
        self.c = 0
        self.total = total
        self.last_flush_step = 0

    def count(self, step=1):

        try:
            self.c += step
            current_flush_step = int(self.c / self.total * 100)
            self.c = min(self.c, self.total)
            # print('current_flush_step', current_flush_step, flush=True)
            if current_flush_step > self.last_flush_step:
                self.last_flush_step = current_flush_step
                print(f'{self.c}/{self.total} done', flush=True)
        except:
            pass


class CrudBase:

    def __init__(self, orm_model, id_field, mysql_user, mysql_password, mysql_host, mysql_port, mysql_database):
        engine = create_engine(
            f'mysql://{mysql_user}:{mysql_password}'
            f'@{mysql_host}:{mysql_port}'
            f'/{mysql_database}'
        )
        session_maker = sessionmaker(bind=engine)
        self.orm_model = orm_model
        self.id_field = id_field
        self.session = session_maker()

    def get(self, id, only_first=True):
        res = self.session.query(self.orm_model).filter(getattr(self.orm_model, self.id_field) == id)
        if only_first:
            return res.first()
        else:
            assert False, "This is not tested yet"
            # return res.all()

    def get_multi(self, skip=0, limit=None):
        return self.session.query(self.orm_model).offset(skip).limit(limit).all()

    def get_multi_filter(self, field, value, skip=0, limit=None, operator='eq'):
        if operator == 'eq':
            return self.session.query(self.orm_model).filter(getattr(self.orm_model, field) == value) \
                .offset(skip).limit(limit).all()
        elif operator == 'gq':
            return self.session.query(self.orm_model).filter(getattr(self.orm_model, field) >= value) \
                .offset(skip).limit(limit).all()
        else:
            assert False, "operator not supported"

    def create(self, obj_in):
        db_obj = self.orm_model(**obj_in)
        self.session.add(db_obj)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            return None
        return db_obj

    def upsert(self, obj_in):
        db_obj = self.orm_model(**obj_in)
        self.session.merge(db_obj)
        self.session.commit()
        return db_obj

    def create_multi(self, data_list, batch_size=100):
        if not isinstance(data_list, list):
            data_list = list(data_list)
        counter = Counter(total=len(data_list))
        i = 0
        db_obj_list = []
        while i < len(data_list):
            counter.count(batch_size)
            batch_data = data_list[i:i + batch_size]
            i += batch_size
            batch_db_obj_list = [self.orm_model(**dict(obj)) for obj in batch_data]
            self.session.add_all(batch_db_obj_list)
            self.session.commit()
            db_obj_list += batch_db_obj_list
        return db_obj_list

    def commit_multi(self, ob_list, batch_size=100):
        if not isinstance(ob_list, list):
            data_list = list(ob_list)
        counter = Counter(total=len(ob_list))
        i = 0
        while i < len(ob_list):
            counter.count(batch_size)
            batch_obs = ob_list[i:i + batch_size]
            i += batch_size
            self.session.add_all(batch_obs)
            self.session.commit()

    def update(self, db_obj, obj_in):

        if db_obj is None:
            assert False

        assert isinstance(db_obj, self.orm_model)

        for field in obj_in:
            setattr(db_obj, field, obj_in[field])
        self.session.add(db_obj)
        self.session.commit()
        return db_obj

    def remove(self, id):
        obj = self.session.query(self.orm_model).get(id)
        if obj is None:
            return None
        self.session.delete(obj)
        self.session.commit()
        return obj

    def delete_all(self):
        try:
            num_rows_deleted = self.session.query(self.orm_model).delete()
            self.session.commit()
            print("deleted " + str(num_rows_deleted) + " rows from " + self.orm_model.__tablename__)
        except Exception as ex:
            print("could not delete rows" + str(ex))
            self.session.rollback()

    def delete_filter(self, field, value, operator='eq'):
        try:

            if operator == 'eq':
                num_rows_deleted = self.session.query(self.orm_model).filter(getattr(self.orm_model, field) == value) \
                    .delete()
            elif operator == 'gq':
                num_rows_deleted = self.session.query(self.orm_model).filter(getattr(self.orm_model, field) >= value) \
                    .delete()
            elif operator == 'lq':
                num_rows_deleted = self.session.query(self.orm_model).filter(getattr(self.orm_model, field) <= value) \
                    .delete()
            else:
                assert False, "operator not supported"
            self.session.commit()
            print("deleted " + str(num_rows_deleted) + " rows from " + self.orm_model.__tablename__)
        except Exception as ex:
            print("could not delete rows" + str(ex))
            self.session.rollback()
