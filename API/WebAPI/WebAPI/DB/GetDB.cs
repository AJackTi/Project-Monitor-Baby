using System.Collections.Generic;
using System.Data;
using System.Data.SQLite;
using System.Linq;

namespace WebAPI.DB
{
    public class GetDB
    {
        private static InitDB initDB;
        private static SQLiteCommand sql_cmd;
        private static SQLiteConnection sql_con;
        private static SQLiteDataAdapter DB;
        private static DataSet DS = new DataSet();
        private static DataTable DT = new DataTable();
        public GetDB()
        {
            initDB = new InitDB();
            DB = new SQLiteDataAdapter();
            //initDB.SetConnection();
            sql_cmd = new SQLiteCommand();
        }
        public static DataTable GetAll(string dbTable)
        {
            sql_con = initDB.SetConnection();
            sql_con.Open();
            sql_cmd = sql_con.CreateCommand();
            string CommandText = "select * from " + dbTable;
            DB = new SQLiteDataAdapter(CommandText, sql_con);
            DS.Reset();
            DB.Fill(DS);
            DT = DS.Tables[0];
            return DT;
        }

        public static string ConvertDataTableToString(DataTable dataTable)
        {
            string data = string.Empty;
            for (int i = 0; i < dataTable.Rows.Count; i++)
            {
                DataRow row = dataTable.Rows[i];
                for (int j = 0; j < dataTable.Columns.Count; j++)
                {
                    data += dataTable.Columns[j].ColumnName + "~" + row[j];
                    if (j == dataTable.Columns.Count - 1)
                    {
                        if (i != (dataTable.Rows.Count - 1))
                            data += "$";
                    }
                    else
                        data += "|";
                }
            }
            return data;
        }

        #region Get Data Not Exactly. Using or in this query
        /// <summary>Get Data Not Exactly. Using or with query</summary>
        /// <returns><c>true</c>, if with info was gotten, <c>false</c> otherwise.</returns>
        /// <param name="listOutput">List output.</param>Ex: select username, password
        /// <param name="listInput">List input.</param>Ex: where username=username or password=password
        /// <param name="listParameter">List parameter.</param>Ex: Username, Password
        /// <param name="dbTable">Name's table.</param>
        public static bool GetWithInfo(List<dynamic> listOutput, List<dynamic> listInput, List<dynamic> listParameter, string dbTable)
        {
            sql_con = initDB.SetConnection();
            sql_con.Open();
            sql_cmd = sql_con.CreateCommand();
            string CommandText = "select ";
            //sql_con.Close();
            foreach (dynamic item in listOutput)
            {
                CommandText += item;
                if (listOutput.ToList().IndexOf(item) != listOutput.Count()-1)
                {
                    CommandText += ", ";
                }
            }
            CommandText += " from " + dbTable + " where ";
            for (int i = 0; i < listInput.Count(); i++)
            {
                CommandText += listParameter.ToList()[i] + "='" + listInput.ToList()[i]+"'";
                if (i!=listInput.Count()-1)
                {
                    CommandText += " or ";
                }
            }
            DB = new SQLiteDataAdapter(CommandText, sql_con);
            DS.Reset();
            DB.Fill(DS);
            DT = DS.Tables[0];
            // Have data
            if (ConvertDataTableToString(DT)!=string.Empty)
            {
                return true;
            }
            // Dont have
            return false;
        }
        #endregion

        #region Get Data Exactly. Using and in this query
        /// <summary>Get Data Not Exactly. Using or with query</summary>
        /// <returns><c>true</c>, if with info was gotten, <c>false</c> otherwise.</returns>
        /// <param name="listOutput">List output.</param>Ex: select username, password
        /// <param name="listInput">List input.</param>Ex: where username=username or password=password
        /// <param name="listParameter">List parameter.</param>Ex: Username, Password
        /// <param name="dbTable">Name's table.</param>
        public static bool GetWithInfoExactly(List<dynamic> listOutput, List<dynamic> listInput, List<dynamic> listParameter, string dbTable)
        {
            sql_con = initDB.SetConnection();
            sql_con.Open();
            sql_cmd = sql_con.CreateCommand();
            string CommandText = "select ";
            //sql_con.Close();
            foreach (dynamic item in listOutput)
            {
                CommandText += item;
                if (listOutput.ToList().IndexOf(item) != listOutput.Count() - 1)
                {
                    CommandText += ", ";
                }
            }
            CommandText += " from " + dbTable + " where ";
            for (int i = 0; i < listInput.Count(); i++)
            {
                CommandText += listParameter.ToList()[i] + "='" + listInput.ToList()[i] + "'";
                if (i != listInput.Count() - 1)
                {
                    CommandText += " and ";
                }
            }
            DB = new SQLiteDataAdapter(CommandText, sql_con);
            DS.Reset();
            DB.Fill(DS);
            DT = DS.Tables[0];
            // Have data
            if (ConvertDataTableToString(DT) != string.Empty)
            {
                return true;
            }
            // Dont have
            return false;
        }
        #endregion
    }
}
