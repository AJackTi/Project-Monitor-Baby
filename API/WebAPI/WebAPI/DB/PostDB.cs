using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SQLite;
using System.Linq;

namespace WebAPI.DB
{
    public class PostDB
    {
        private InitDB initDB;
        private SQLiteCommand sql_cmd;
        private SQLiteConnection sql_con;
        private SQLiteDataAdapter DB;
        private DataSet DS = new DataSet();
        private DataTable DT = new DataTable();
        public PostDB()
        {
            initDB = new InitDB();
            DB = new SQLiteDataAdapter();
            //initDB.SetConnection();
            sql_cmd = new SQLiteCommand();
        }
        private bool Post(IEnumerable<dynamic> listInput, IEnumerable<dynamic> listParameter, string dbName)
        {
            sql_con = initDB.SetConnection();
            sql_con.Open();
            sql_cmd = sql_con.CreateCommand();
            string CommandText = "INSERT INTO " + dbName + "(";
            for (int i = 0; i < listParameter.Count(); i++)
            {
                if (i != listParameter.Count()-1)
                {
                    CommandText += listParameter.ToList()[i] + ", ";
                }
                else
                {
                    CommandText += listParameter.ToList()[i] + ") VALUES(";
                }
            }
            for (int i = 0; i < listInput.Count(); i++)
            {
                if (i != listInput.Count() - 1)
                {
                    CommandText += listInput.ToList()[i] + ", ";
                }
                else
                {
                    CommandText += listParameter.ToList()[i] + ")";
                }
            }
            DB = new SQLiteDataAdapter(CommandText, sql_con);
            DS.Reset();
            //DB.Fill(DS);
            //DT = DS.Tables[0];
            //return DT;
            return false;
        }
    }
}
