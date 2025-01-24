# Open-Cookie-Database for the EDPB Website Auditing Tool

This project converts the [Open Cookie Database](https://github.com/jkwakman/Open-Cookie-Database) for use with the [EDPB Website Auditing Tool](https://code.europa.eu/edpb/website-auditing-tool).

## About Open-Cookie-Database

The [Open Cookie Database](https://github.com/jkwakman/Open-Cookie-Database) is a collaborative effort to describe and categorize major cookies. It supports various research and open-source projects and welcomes [contributions](docs/CONTRIBUTING.md).

## About the EDPB Website Auditing Tool

The [EDPB Website Auditing Tool](https://code.europa.eu/edpb/website-auditing-tool) is a Free Software initiative from the [European Data Protection Board](https://www.edpb.europa.eu). It facilitates website inspections by collecting evidence, analyzing data, and generating reports on trackers used by websites. The tool supports multiple knowledge bases to identify the purposes of these trackers.

## Adaptations to the Open-Cookie-Database

Cookie descriptions from the Open Cookie Database are stored in a [CSV file](open-cookie-database.csv). The equivalent knowledge base for the EDPB Website Auditing Tool is provided in a [JSON file](open-cookie-database-wat.json), which can be imported into the tool via the knowledge section.

The conversion script is available in [Python](.github/workflows/convert_to_wat.py). For more details about the Open Cookie Database format, refer to the [contribution guidelines](docs/CONTRIBUTING.md).

### Key Differences Between the Two Databases

#### Cookie Descriptions

The Open Cookie Database provides the following fields:
- **ID**: Unique identifier for the cookie.
- **Platform**: Platform or service responsible for setting the cookie.
- **Category**: Classification of the cookie (e.g., Functional, Analytics, Marketing).
- **Cookie Name**: Name of the cookie.
- **Domain**: Domain where the cookie is set. This can be a specific value or empty for first-party cookies.
- **Description**: Explanation of the cookie's purpose.
- **Retention Period**: Expiry duration of the cookie.
- **Data Controller**: Company responsible for controlling the data.
- **User Privacy & GDPR**: Link to the privacy policy or GDPR compliance page.
- **Wildcard**: Indicates whether the cookie name is a wildcard (1 for wildcard, 0 otherwise).

In contrast, the EDPB Website Auditing Tool requires the following fields:
- **category**: Purpose of the cookie (e.g., Targeted advertising, Analytics, Social media). Open-Cookie-Database categories are retained as a basis.
- **domain**: URL domain of the cookie origin, using wildcards (e.g., `*.adcompany.com` for third-party cookies, `*` for first-party cookies).
- **name**: Identifier of the cookie, allowing wildcards (e.g., `RTB_*` for cookies like `RTB_1234` and `RTB_5678`).
- **source**: Origin or identification source.
- **controller**: Data controller responsible for the processing (use `?` if unknown).
- **policy**: Link to the privacy policy, if available.
- **reference**: References, such as existing sanctions, if applicable.
- **comment**: Additional contextual information about the cookie.

#### Category Descriptions

The Open-Cookie-Database defines categories as follows:
- **Functional**: Also known as technical, essential, or strictly necessary.
- **Personalization**: Also known as preferences.
- **Analytics**: Also known as performance or statistics.
- **Marketing**: Also known as tracking or social media.
- **Security**: Cookies related to security purposes.

#### Wildcard Match

In the Open-Cookie-Database, the "Wildcard match" column uses `0` for non-wildcard cookie names and `1` for wildcard names.  
The EDPB Website Auditing Tool directly supports wildcards in cookie names. For example, `_gac_*` represents a wildcard, as the `*` can match any string.

## How to Convert the Database

Run the following command to convert the database:
```bash
python .github/workflows/convert_to_wat.py