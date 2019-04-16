using System;
using System.Data;
using System.Data.SQLite;

namespace WebAPI.DB
{
    public class InitDB
    {
        private SQLiteConnection sql_con;
        private SQLiteCommand sql_cmd;
        private DataSet DS = new DataSet();
        private DataTable DT = new DataTable();
        public SQLiteConnection SetConnection(string database="test.db")
            {
            sql_con = new SQLiteConnection
                ("Data Source="+ database + ";Version=3;New=False;Compress=True;");
            return sql_con;
        }
        public void ExecuteQuery(string txtQuery)
        {
            SetConnection();
            sql_con.Open();
            sql_cmd = sql_con.CreateCommand();
            sql_cmd.CommandText = txtQuery;
            sql_cmd.ExecuteNonQuery();
            sql_con.Close();
        }
    }
}
