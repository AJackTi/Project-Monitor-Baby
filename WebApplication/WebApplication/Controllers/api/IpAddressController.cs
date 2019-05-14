using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace WebApplication.Controllers.api
{
    [Produces("application/json")]
    [Route("api/[controller]")]
    public class IpAddressController : Controller
    {
        // GET: api/values
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/values/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            return "value";
        }

        public class IpAddress
        {
            public string ipAddress { get; set; }
            public int port { get; set; }
            public DateTime timeRegist { get; set; }
            public int frequency { get; set; }
        }

        // POST api/values
        [HttpPost]
        public bool Post([FromBody]string name)
        {
            var data = new IpAddress();
            data.ipAddress = name.Split(":")[0];
            data.timeRegist = DateTime.Now;
            data.frequency = 1;
            data.port = int.Parse(name.Split(":")[1]);
            if (CheckDuplicateJson("data.json", name.Split(":")[0]))
            {
                // cộng thêm vào số lần(frequency)
                // lấy số lần hiện tại += 1
                data.frequency = PlusFrequency("data.json", data.ipAddress) + 1;
                
            }
            WriteToJsonFile("data.json", data, true);
            return CheckExistFile("data.json");
        }
        /// <summary>
        /// Check file exist
        /// </summary>
        /// <param name="filePath"></param>
        /// <returns></returns>
        public static bool CheckExistFile(string filePath)
        {
            if (System.IO.File.Exists(filePath))
            {
                return true;
            }
            return false;
        }

        /// <summary>
        /// Writes the given object instance to a Json file.
        /// <para>Object type must have a parameterless constructor.</para>
        /// <para>Only Public properties and variables will be written to the file. These can be any type though, even other classes.</para>
        /// <para>If there are public properties/variables that you do not want written to the file, decorate them with the [JsonIgnore] attribute.</para>
        /// </summary>
        /// <typeparam name="T">The type of object being written to the file.</typeparam>
        /// <param name="filePath">The file path to write the object instance to.</param>
        /// <param name="objectToWrite">The object instance to write to the file.</param>
        /// <param name="append">If false the file will be overwritten if it already exists. If true the contents will be appended to the file.</param>
        public static void WriteToJsonFile<T>(string filePath, T objectToWrite, bool append = false) where T : new()
        {
            TextWriter writer = null;
            try
            {
                var contentsToWriteToFile = JsonConvert.SerializeObject(objectToWrite);
                writer = new StreamWriter(filePath, append);
                writer.Write(contentsToWriteToFile);
            }
            finally
            {
                if (writer != null)
                    writer.Close();
            }
        }

        /// <summary>
        /// Check duplicate frequency with this ip in file
        /// </summary>
        /// <param name="filePath"></param>
        /// <returns></returns>
        public static bool CheckDuplicateJson(string filePath, string ipAddress)
        {
            var data = GetIpaddressJsonFile(filePath);
            if (data.Any())
            {
                return data.Contains(ipAddress);
            }
            return false;
        }

        public static List<string> GetIpaddressJsonFile(string filePath)
        {
            if (!CheckExistFile(filePath))
            {
                return new List<string>();
            }
            using (StreamReader r = new StreamReader(filePath))
            {
                string json = r.ReadToEnd();
                var items = JsonConvert.DeserializeObject<RootObject>(json);
                return items.ipAddresses.Select(t => t.ipAddress).ToList();
            }
        }

        public static int PlusFrequency(string filePath, string ipAddress)
        {
            using (StreamReader r = new StreamReader(filePath))
            {
                string json = r.ReadToEnd();
                var items = JsonConvert.DeserializeObject<RootObject>(json);
                try
                {
                    return items.ipAddresses.ToList().Where(t => t.ipAddress == ipAddress).FirstOrDefault().frequency;
                }
                catch (Exception)
                {
                    return -1;
                }
            }
            return -1;
        }

        public class RootObject
        {
            public List<IpAddress> ipAddresses { get; set; }
        }

        /// <summary>
        /// Reads an object instance from an Json file.
        /// <para>Object type must have a parameterless constructor.</para>
        /// </summary>
        /// <typeparam name="T">The type of object to read from the file.</typeparam>
        /// <param name="filePath">The file path to read the object instance from.</param>
        /// <returns>Returns a new instance of the object read from the Json file.</returns>
        public static T ReadFromJsonFile<T>(string filePath) where T : new()
        {
            TextReader reader = null;
            try
            {
                reader = new StreamReader(filePath);
                var fileContents = reader.ReadToEnd();
                return JsonConvert.DeserializeObject<T>(fileContents);
            }
            finally
            {
                if (reader != null)
                    reader.Close();
            }
        }
    }
}
