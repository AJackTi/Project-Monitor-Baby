using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Caching.Memory;
using System.Collections.Generic;

namespace WebApplication.Controllers.api
{
    [Route("api/[controller]")]
    [ApiController]
    public class LoginController : ControllerBase
    {
        public IMemoryCache _cache;
        public static List<string> listUserSession;
        public LoginController(IMemoryCache memoryCache)
        {
            _cache = memoryCache;
            listUserSession = new List<string>();
        }
        
        // GET: api/Login
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET: api/Login/5
        [HttpGet("{id}", Name = "Get")]
        public string Get(int id)
        {
            return "value";
        }

        // POST: api/Login
        [HttpPost]
        public bool Post([FromBody] string value)
        {
            bool isExist;
            if (!_cache.TryGetValue(value, out isExist))
            {
                _cache.Set(value, isExist);
                listUserSession.Add(value);
                return true;
            }
            return false;
        }

        // PUT: api/Login/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE: api/ApiWithActions/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}