# coding: utf-8
"""
SQLAlchemy　実行モジュール
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scope_session
from conf import aws_config
from common import logger


def init(user, host, database, password=None, echo=True, autocommit=True,
         autoflush=True, poolsize=10, maxoverflow=5, poolrecycle=10):
    """
    データベース接続初期化関数

    Parameters
    -------
    user : str
        ユーザー名
    host : str
        接続先ホスト名
    database : str
        接続先データベース名
    password : str
        パスワード
    echo : boolean
        ログ出力設定
        True : ログ出力あり
        Flase : ログ出力なし
    autocommit : boolean
        オートコミット設定
        True : オートコミット
        False : オートコミットなし
    autoflush : boolean
        オートフラッシュ設定
        True : オートフラッシュ
        False : オートフラッシュなし
    poolsize : int
        コネクションプーリング数
    maxoverflow : int
        コネクションオーバーフロー数
    poolrecycle : int
        コネクション再利用数

    Returns
    -------
    session : sqlalchemy.orm.sessionmaker.sessionmaker
        データベースセッション
    engine : sqlalchemy.engine.Engine
        データベースエンジン
    """
    # URLの作成
    if password is None:
        url = 'mysql+pymysql://' + user +\
            '@' + host + '/' + database + '?charset=utf8'
    else:
        url = 'mysql+pymysql://' + user + ':' + password + \
            '@' + host + '/' + database + '?charset=utf8'
    # エンジンクラスの作成
    engine = create_engine(
        url, echo=echo, pool_size=poolsize, max_overflow=maxoverflow,
        pool_recycle=poolrecycle)
    # セッションの作成
    Session = scope_session(sessionmaker(
        autocommit=autocommit, autoflush=autoflush, bind=engine))
    session = Session()
    return session, engine


def add_data(session, object):
    """
    INSERT実行関数

    Parameters
    ----------
    session : sqlalchemy.orm.sessionmaker.sessionmaker
        データベースセッション
    object : model.
        格納データオブジェクト
    """
    # オブジェクトの格納
    session.add(object)


def commit(session):
    """
    コミット関数

    Parameters
    ----------
    session : sqlalchemy.orm.sessionmaker.sessionmaker
        データベースセッション
    """
    # コミット
    session.commit()


def close(session, engine):
    """
    クローズ関数

    Parameters
    ----------
    session : sqlalchemy.orm.sessionmaker.sessionmaker
        データベースセッション
    engine : sqlalchemy.engine.Engine
        データベースエンジン
    """
    # セッションのクローズ
    session.expunge_all()
    engine.dispose()


def commit_close(session, engine):
    """
    コミット＆クローズ関数

    Parameters
    ----------
    session : sqlalchemy.orm.sessionmaker.sessionmaker
        データベースセッション
    engine : sqlalchemy.engine.Engine
        データベースエンジン
    """
    # コミット
    parent = session.commit()
    # セッションのクローズ
    session.expunge_all()
    engine.dispose()
