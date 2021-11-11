from sqlalchemy import exc
import json
class Persistence():
    def __init__(self, config, myApp, myDb):
        self.myApp = myApp
        self.myApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.myDb = myDb
        self.config = config
        self.mySession = [1,1]
    """
       Métodos SQL Core 
    """
# TESTED

    def _sql(self, rawSql):
        try:
            assert type(rawSql) == str
            # assert type(sqlVars) == dict
            res = self._sqltran(rawSql)
            if res is not None:
                self.myDb.session.commit()
            return res
        except exc.SQLAlchemyError as e:
            print(e)
        
# TESTED

    def _sqltran(self, rawSql):
        try:
            assert type(rawSql) == str
            # assert type(sqlVars) == dict
            cursor = self.myDb.session.execute(rawSql)
            session = self.myDb.session
            return {"cursor": cursor, "session": session}
        except exc.SQLAlchemyError as e:
            print(e)
 
# TESTED

    def setWrite(self, stm, table, register=False, logtable="log", loglevel=1, logtype=1):
        self.config.core.getEnvCnx(table)
        res = self._sqltran(stm)
        if res is not None and register:
            self.setWriteLog(stm, logtable, loglevel, logtype)
        return res
# TESTED

    def setWriteLog(self, stm, logtable="log", loglevel=1, logtype=1):
        insert = "INSERT INTO " + logtable + """(description,log_level_id_fk,log_type_id_fk,user_id_fk)
             VALUES ('""" + str(stm) + "#"+str(self.mySession)+"',"+str(loglevel)+","+str(logtype)+","+str(self.mySession[0])+")"
        self.config.core.getEnvCnx(logtable)
        res = self._sqltran(insert)
        return res

    def spExec(self, sp, args):
        stm = "CALL "+sp+"("+args+")"
        return self._sql(stm)

    def setProp(self, table, key, value, condition):
        if condition:
            stm = "UPDATE "+table+" SET props = jsonb_set(props, "+key+", '"+value+"' ,false) \
                FROM "+table+" \
                WHERE "+condition+""
            return self._sql(stm)
    """
       GETTERS
    """

    def getPaginatedQuery(self, stm, table, field, since, top):
        condition = (lambda x: "AND"
                     if (str(x).upper().contains("WHERE")) else "WHERE")(stm)
        pStm = stm+" "+condition+" "+field+" > "+since + " LIMIT "+top
        res = self.getQuery(pStm, table)
        return res
# TESTED

    def getProps(self, table, condition="1=1"):
        stm = "SELECT props from public.\""+table+"\" Where "+condition
        print(stm)
        res = self.getQuery(stm, table)
        return res[0]['props']
# TESTED

    def getNextVal(self, field, table):
        stm = "SELECT MAX("+field+") FROM "+table+""
        res = self.getQuery(stm, table)
        return res[0]
# TESTED

    def getUserPermission(self, userid, table='permission'):
        stm = """ SELECT prm.* FROM public.\""""+table + """\" prm 
                JOIN public.\"profile\" prf 
                ON prm.profile_id_fk = prf.id 
                JOIN public.\"profile_user\" prfUsr
                ON prfUsr.profile_id_fk = prf.id
                JOIN public.\"user\" usr 
                ON  prfUsr.user_id_fk =usr.id
                WHERE  usr.id = """ + userid
        res = self.getQuery(stm, table)
        return res
# TESTED

    def getParam(self,  session, table='param',  key=None,):
        stm = """SELECT prm.* FROM
               public.\"""" + table + """\" prm 
                JOIN public.\"param_institution\" prmInst 
                ON prmInst.param_id_fk=prm.id
                JOIN public.\"institution\" ins 
                ON ins.id = prmInst.institution_id_fk
                WHERE ins.id = """+session[0]+(lambda x: " AND prm.key="+key if (x is not None) else "")(key)
        res = self.getQuery(stm, table)
        return res
# TESTED
    def existValue(value, replacement):
        if value != "" and value != None:
            return "'"+value+"'"
        return replacement

    def getQuery(self, stm, table):
        self.config.core.getEnvCnx(table)
        res = self._sql(stm)
        return self.convert(res['cursor'].fetchall())
    def getStm(self, stm, table):
        self.config.core.getEnvCnx(table)
        res = self._sql(stm)
        return res

    def convert(self, res):
        data = ""
        if isinstance(res, list):
            l = []
            for i in res:
                d = dict(i)
                l.append(d)
            data = l
        return json.loads(json.dumps(data, indent=4, sort_keys=True, default=str))