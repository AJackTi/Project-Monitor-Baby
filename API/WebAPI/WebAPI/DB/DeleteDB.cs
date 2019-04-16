using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SQLite;
using System.Linq;

namespace WebAPI.DB
{
    public class DeleteDB
    {
        private InitDB initDB;
        private SQLiteCommand sql_cmd;
        private SQLiteConnection sql_con;
        private SQLiteDataAdapter DB;
        private DataSet DS = new DataSet();
        private DataTable DT = new DataTable();
        public DeleteDB()
        {
            initDB = new InitDB();
            DB = new SQLiteDataAdapter();
            //initDB.SetConnection();
            sql_cmd = new SQLiteCommand();
        }

        private bool DeleteInfo(IEnumerable<dynamic> listInput, IEnumerable<dynamic> listParameter, string dbName)
        {
            sql_con = initDB.SetConnection();
            sql_con.Open();
            sql_cmd = sql_con.CreateCommand();
            string CommandText = "DELETE FROM " + dbName + "WHERE ";
            for (int i = 0; i < listParameter.Count(); i++)
            {
                CommandText += listParameter.ToList()[i] + "=" + listInput.ToList()[i];
                if (i != listParameter.Count()-1)
                {
                    CommandText += " and ";
                }
            }
            DB = new SQLiteDataAdapter(CommandText, sql_con);
            // Check it's deleted successfully
            //DS.Reset();
            //DB.Fill(DS);
            //DT = DS.Tables[0];
            //return DT;
            return false;
        }
    }
}
