from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import load_only
from flask.json import jsonify


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/ms_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)


class Ktdef(db.Model):
    __tablename__ = 'ktdef'
    id = db.Column(db.String,primary_key=True,doc='id')
    typeName = db.Column(db.String,doc='类型名称')
    typeTableDef = db.Column(db.String,doc='类型对应表明')
    typeFieldsDef = db.Column(db.String,doc='类型对应的字段')


class Detail_Comment(db.Model):
    __tablename__ = 'detail_comment'
    id = db.Column(db.String,primary_key=True,doc='id')
    keyObj = db.Column(db.String,doc='评论对象')
    speaker = db.Column(db.String,doc='评论人')
    commentDate = db.Column(db.DateTime,doc='评论时间')
    comment = db.Column(db.String,doc='评论内容')

    def dic(self):
        return {'id':self.id,
                'keyObj':self.keyObj,
                'speaker':self.speaker,
                'commentDate':self.commentDate.strftime('%Y-%m-%d'),
                "comment":self.comment}



@app.route('/',methods=['GET','POST'])
def getComment():
    tableName = request.args.get('tableName')
    data = db.session.query(Ktdef).options(load_only(Ktdef.typeTableDef,Ktdef.typeFieldsDef)).filter(Ktdef.typeName == tableName).first()
    name = data.typeTableDef
    tname = eval(data.typeTableDef)
    fields = data.typeFieldsDef
    fields_list = fields.split(';')

    comments = db.session.query(tname).options(load_only(*fields_list)).all()
    data = []
    for comment in comments:
        dic = {}
        for col in fields_list:
            dic[col] = comment.dic().get(col)
        data.append(dic)

    return jsonify(tableName=name,data=data)




if __name__ == '__main__':
    app.run()